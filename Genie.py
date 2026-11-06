# Databricks notebook source
# MAGIC %md
# MAGIC <img src="data:image/png;base64,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" alt="Databricks" height="32">&nbsp;&nbsp;&nbsp;&nbsp;<img src="data:image/png;base64,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" alt="Genie" height="48">
# MAGIC
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
