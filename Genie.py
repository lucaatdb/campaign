# Databricks notebook source
# MAGIC %md
# MAGIC # Genie playbook: getting governed data to business users
# MAGIC
# MAGIC > **Before you start:** this notebook is a starting point, not a supported product. Preview features (marked **Preview** or **Beta**) need an admin to enable them and may change. Run each cell only after reading it; cells that create or change objects are clearly labelled. Questions? Reply to the email that sent you here.
# MAGIC
# MAGIC <a id="contents"></a>
# MAGIC ## Contents
# MAGIC Click a section to jump to it. You can also open the built-in **table of contents** panel with the icon at the top left of the notebook; every section and code step appears there.
# MAGIC
# MAGIC - [**0. Shared prep: make your tables Genie-ready**](#section-0)
# MAGIC   - Read-only: list tables and columns in the schema that have no description…
# MAGIC   - CHANGES METADATA: fill in your own descriptions, then set RUN = True
# MAGIC - [**1. Genie in Microsoft Teams on top of a Power BI gold layer**](#section-1)
# MAGIC   - Read-only: check who can read the gold tables
# MAGIC   - CHANGES PERMISSIONS: give a business-user group read access to the gold…
# MAGIC - [**2. Genie One in Excel and Google Sheets for spreadsheet teams**](#section-2)
# MAGIC   - CREATES A VIEW: a curated, spreadsheet-friendly view
# MAGIC   - Install dbdemos
# MAGIC   - List and install a demo
# MAGIC - [**3. Embedding Genie answers and charts in your own product**](#section-3)
# MAGIC   - Calls the Genie One API
# MAGIC - [**4. Genie One Chat for staff self-service**](#section-4)
# MAGIC - [**5. Scheduled Genie Code tasks for recurring checks on POC and dev work**](#section-5)
# MAGIC
# MAGIC **Start with the setup cell below** (choose catalog and schema), then go to your section.

# COMMAND ----------

# DBTITLE 1,Setup: choose catalog and schema
# Set where you want to work. Nothing in this notebook changes data until you run a cell that says it does.
dbutils.widgets.text("catalog", "main", "Catalog")
dbutils.widgets.text("schema", "default", "Schema")
CATALOG = dbutils.widgets.get("catalog")
SCHEMA = dbutils.widgets.get("schema")
print(f"Working in {CATALOG}.{SCHEMA}")

# COMMAND ----------

# MAGIC %md
# MAGIC <a id="section-0"></a>
# MAGIC ## 0. Shared prep: make your tables Genie-ready
# MAGIC Genie answers improve most when tables and columns have clear descriptions. These cells find gold tables with missing comments and help you add them. Do this before you set up any Genie Agent.
# MAGIC
# MAGIC [↑ Back to contents](#contents)

# COMMAND ----------

# DBTITLE 1,Read-only: list tables and columns in the schema that have no description…
# Read-only: list tables and columns in the schema that have no description yet.
missing_tables = spark.sql(f"""
  SELECT table_name, comment
  FROM {CATALOG}.information_schema.tables
  WHERE table_schema = '{SCHEMA}' AND (comment IS NULL OR comment = '')
""")
missing_cols = spark.sql(f"""
  SELECT table_name, column_name, data_type
  FROM {CATALOG}.information_schema.columns
  WHERE table_schema = '{SCHEMA}' AND (comment IS NULL OR comment = '')
  ORDER BY table_name, ordinal_position
""")
display(missing_tables); display(missing_cols)

# COMMAND ----------

# DBTITLE 1,CHANGES METADATA: fill in your own descriptions, then set RUN = True
# CHANGES METADATA: fill in your own descriptions, then set RUN = True.
RUN = False
table_comments = {
    # "gold_matters": "One row per legal matter, refreshed nightly from the practice management system.",
}
column_comments = {
    # ("gold_matters", "billed_hours"): "Hours billed to the client in the reporting month.",
}
if RUN:
    for t, c in table_comments.items():
        spark.sql(f"COMMENT ON TABLE {CATALOG}.{SCHEMA}.{t} IS '{c}'")
    for (t, col), c in column_comments.items():
        spark.sql(f"ALTER TABLE {CATALOG}.{SCHEMA}.{t} ALTER COLUMN {col} COMMENT '{c}'")
    print("Comments applied.")
else:
    print("Dry run: set RUN = True to apply.")

# COMMAND ----------

# MAGIC %md
# MAGIC **Then create a Genie Agent** in the UI: **Genie > New**, add the tables above, write 3-5 example SQL queries for the questions people ask most, and add a few benchmark questions you can re-run to check accuracy.
# MAGIC Docs: *Curate an effective Genie Agent*.

# COMMAND ----------

# MAGIC %md
# MAGIC <a id="section-1"></a>
# MAGIC ## 1. Genie in Microsoft Teams on top of a Power BI gold layer
# MAGIC **The idea:** Power BI stays the home for reports. People who just need a quick answer ask `@Databricks Genie` in a Teams chat or channel, and the answer comes from the same governed gold tables. Unity Catalog permissions still apply.
# MAGIC
# MAGIC **Status:** Public Preview.
# MAGIC
# MAGIC **What you need (in order):**
# MAGIC 1. An **account admin** MUST enable the *Databricks Genie for Microsoft Teams* preview in the account console (**Previews** page).
# MAGIC 2. A **Microsoft 365 admin** installs **Databricks Genie** from the Microsoft marketplace and approves the app permissions.
# MAGIC 3. If the workspace uses an IP access list or Private Link, follow the extra steps in the docs page *Databricks Genie app in Microsoft Teams*.
# MAGIC 4. Complete section 0 on the gold tables and create a Genie Agent for them.
# MAGIC
# MAGIC **Make it topic-specific:** in a Teams channel, the channel owner can **pin a Genie Agent** so every question in that channel goes to that agent, for example a "Matters & billing" agent for a practice-management channel.
# MAGIC
# MAGIC [↑ Back to contents](#contents)

# COMMAND ----------

# DBTITLE 1,Read-only: check who can read the gold tables
# Read-only: check who can read the gold tables. Teams users only see what Unity Catalog lets them see.
display(spark.sql(f"SHOW GRANTS ON SCHEMA {CATALOG}.{SCHEMA}"))

# COMMAND ----------

# DBTITLE 1,CHANGES PERMISSIONS: give a business-user group read access to the gold…
# CHANGES PERMISSIONS: give a business-user group read access to the gold schema. Set RUN = True to apply.
RUN = False
GROUP = "practice-managers"   # an existing account group
if RUN:
    spark.sql(f"GRANT USE CATALOG ON CATALOG {CATALOG} TO `{GROUP}`")
    spark.sql(f"GRANT USE SCHEMA, SELECT ON SCHEMA {CATALOG}.{SCHEMA} TO `{GROUP}`")
    print("Granted.")
else:
    print("Dry run.")

# COMMAND ----------

# MAGIC %md
# MAGIC <a id="section-2"></a>
# MAGIC ## 2. Genie One in Excel and Google Sheets for spreadsheet teams
# MAGIC **The idea:** your data is already modeled with SQL and scheduled jobs. Project and operations teams ask questions in plain English from **Excel** or **Google Sheets** and pull governed results straight into their sheet.
# MAGIC
# MAGIC **What you need:**
# MAGIC * **Excel:** install and configure the **Databricks Excel Add-in** (docs: *Set up the Excel Add-in*), then click the **Genie** icon in the add-in pane (docs: *Use Genie One in Microsoft Excel*).
# MAGIC * **Google Sheets:** install the **Databricks Connector for Google Sheets** and open Genie One from it (docs: *Use Genie One in Google Sheets*).
# MAGIC * Users MUST have access to Genie One and SELECT on the tables.
# MAGIC
# MAGIC **Tip:** give spreadsheet users a small, curated set of views with business-friendly names instead of raw tables. The cell below creates one.
# MAGIC
# MAGIC [↑ Back to contents](#contents)

# COMMAND ----------

# DBTITLE 1,CREATES A VIEW: a curated, spreadsheet-friendly view
# CREATES A VIEW: a curated, spreadsheet-friendly view. Edit the SELECT for your data, then set RUN = True.
RUN = False
VIEW = "v_project_costs_monthly"
SQL = f"""
CREATE OR REPLACE VIEW {CATALOG}.{SCHEMA}.{VIEW}
COMMENT 'Monthly cost per project, for Excel/Sheets users.'
AS SELECT
  project_id   AS `Project`,
  month        AS `Month`,
  SUM(amount)  AS `Cost`
FROM {CATALOG}.{SCHEMA}.fact_costs   -- replace with your table
GROUP BY ALL
"""
if RUN:
    spark.sql(SQL); print(f"Created {VIEW}")
else:
    print(SQL)

# COMMAND ----------

# MAGIC %md
# MAGIC **Want to see it working before using your own data?** The open-source `dbdemos` library installs a complete AI/BI demo (dashboards plus a Genie Agent) into your workspace. Demo names can change, so list them first.

# COMMAND ----------

# DBTITLE 1,Install dbdemos
# MAGIC %pip install --quiet dbdemos
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# DBTITLE 1,List and install a demo
import dbdemos
dbdemos.list_demos()   # confirm the demo name exists, e.g. an "aibi-..." demo
# dbdemos.install("aibi-supply-chain-forecasting", path="./dbdemos")   # uncomment to install

# COMMAND ----------

# MAGIC %md
# MAGIC <a id="section-3"></a>
# MAGIC ## 3. Embedding Genie answers and charts in your own product
# MAGIC **The idea:** your application sends a user's question to a **Genie Agent** and shows the answer in your own UI: the text, the result data and, since August 2026, the **visualization** Genie generated. Unity Catalog permissions on the Genie Agent's tables decide what each caller can see.
# MAGIC
# MAGIC **Two APIs:**
# MAGIC * **Genie Agents API (Chat mode / Conversation API):** for one specific Genie Agent. Start a conversation, send follow-ups, and retrieve the generated SQL, query results and visualizations. Docs: *Use the Genie Agents API*, plus the Conversation API reference.
# MAGIC * **Genie One API:** to ask across all the data a user can access. Docs: *Use the Genie One API*.
# MAGIC
# MAGIC **What you need:** a Genie Agent (see section 0) and its ID (from the agent's URL), plus a service principal or user identity for your app. For a multi-tenant product, give each customer their own identity, or a Genie Agent whose permissions only cover that customer's data.
# MAGIC
# MAGIC [↑ Back to contents](#contents)

# COMMAND ----------

# DBTITLE 1,Calls the Genie One API
# Calls the Genie One API (read-only question). Example adapted from the "Use the Genie One API" docs page.
import json, requests
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
base_url = f"{w.config.host}/api/2.0/genie/one"

def ask_genie_one(question, conversation_id=None):
    body = {"input": question}
    if conversation_id:
        body["conversation_id"] = conversation_id
    with requests.post(f"{base_url}/responses",
                       headers={**w.config.authenticate(), "Content-Type": "application/json"},
                       json=body, stream=True) as resp:
        resp.raise_for_status()
        resp.encoding = "utf-8"
        for line in resp.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue
            data = line[5:].lstrip(" ")
            if data == "[DONE]":
                break
            event = json.loads(data)
            if event["type"] in ("response.completed", "response.failed", "response.incomplete"):
                return event["response"]

r = ask_genie_one("What were the top 5 products by revenue last month?")
for item in r["output"]:
    if item.get("phase") == "final_answer":
        print("\n\n".join(part["text"] for part in item["content"]))

# COMMAND ----------

# MAGIC %md
# MAGIC **For a single Genie Agent (what you embed in a product)**, use the Conversation API. The Databricks CLI wraps it, which makes it a quick way to test from a terminal:
# MAGIC ```bash
# MAGIC databricks genie start-conversation <GENIE_AGENT_ID> "How many active members do we have by state?"
# MAGIC ```
# MAGIC For the endpoints that return query results and **visualizations**, use the *Conversation API reference* linked from *Use the Genie Agents API*. The visualization retrieval endpoint is GA as of August 2026.

# COMMAND ----------

# MAGIC %md
# MAGIC <a id="section-4"></a>
# MAGIC ## 4. Genie One Chat for staff self-service
# MAGIC **The idea:** one place where staff ask questions in plain English across your **Genie Agents, dashboards, saved queries and metric views**, without needing to know which asset holds the answer. Genie One Chat is GA (June 2026).
# MAGIC
# MAGIC **What you need:**
# MAGIC 1. Complete section 0 on the tables your team maintains.
# MAGIC 2. Create at least one Genie Agent, plus any dashboards you already use.
# MAGIC 3. Users need workspace access with Genie One and SELECT on the data (the grant cell in section 1 works here too).
# MAGIC
# MAGIC **See it first:** install an AI/BI demo with `dbdemos` (section 2 cells) and open Genie One to try questions against it.
# MAGIC
# MAGIC [↑ Back to contents](#contents)

# COMMAND ----------

# MAGIC %md
# MAGIC <a id="section-5"></a>
# MAGIC ## 5. Scheduled Genie Code tasks for recurring checks on POC and dev work
# MAGIC **The idea:** schedule a recurring natural-language prompt. Each run is a full Genie Code session in your workspace and leaves a chat your team can pick up. It suits the small recurring chores around POCs that don't justify a job each. Genie Code scheduled tasks are GA (September 2026).
# MAGIC
# MAGIC **Example prompts to schedule:**
# MAGIC * *"Profile yesterday's loads in `<catalog>.<schema>`: row counts, null rates on key columns, and anything that moved more than 20% versus the prior day."*
# MAGIC * *"Re-run the notebook `<path>` against the demo dataset and tell me if any cell fails."*
# MAGIC * *"List tables in `<catalog>.<schema>` that haven't been updated in 7 days."*
# MAGIC
# MAGIC **How:** open **Genie Code**, write the prompt, and use the schedule option to set the frequency. Docs: *Genie Code* (scheduled tasks).
# MAGIC
# MAGIC **Starter kits for client POCs:**
# MAGIC * `dbdemos` (cells in section 2) installs complete Databricks demos into a workspace.
# MAGIC * Bundle templates give each new client project a deployable starting structure. Run these from your terminal with the Databricks CLI:
# MAGIC ```bash
# MAGIC databricks bundle init default-python   # job + ETL pipeline project
# MAGIC databricks bundle deploy -t dev
# MAGIC ```
# MAGIC
# MAGIC [↑ Back to contents](#contents)
