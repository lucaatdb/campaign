# Databricks notebook source
# MAGIC %md
# MAGIC <div style="display:flex; align-items:center; gap:32px; padding:16px 24px; background-color:#F9F7F4; border-radius:8px;">
# MAGIC   <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzEzIiBoZWlnaHQ9IjExMyIgdmlld0JveD0iMCAwIDcxMyAxMTMiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8xOTg0XzczMykiPgo8cGF0aCBkPSJNOTguOSA0Ni41OTk2TDUyLjMgNzIuODk5NkwyLjQgNDQuNzk5NkwwIDQ2LjA5OTZWNjYuNDk5Nkw1Mi4zIDk1Ljg5OTZMOTguOSA2OS42OTk2VjgwLjQ5OTZMNTIuMyAxMDYuOEwyLjQgNzguNjk5NkwwIDc5Ljk5OTZWODMuNDk5Nkw1Mi4zIDExMi45TDEwNC41IDgzLjQ5OTZWNjMuMDk5NkwxMDIuMSA2MS43OTk2TDUyLjMgODkuNzk5Nkw1LjYgNjMuNTk5NlY1Mi43OTk2TDUyLjMgNzguOTk5NkwxMDQuNSA0OS41OTk2VjI5LjQ5OTZMMTAxLjkgMjcuOTk5Nkw1Mi4zIDU1Ljg5OTZMOCAzMS4wOTk2TDUyLjMgNi4xOTk2MUw4OC43IDI2LjY5OTZMOTEuOSAyNC44OTk2VjIyLjM5OTZMNTIuMyAwLjA5OTYwOTRMMCAyOS40OTk2VjMyLjY5OTZMNTIuMyA2Mi4wOTk2TDk4LjkgMzUuNzk5NlY0Ni41OTk2WiIgZmlsbD0iI0ZGMzYyMSIvPgo8cGF0aCBkPSJNMjAyLjIgOTYuMTk5NFY2LjM5OTQxSDE4OC40VjM5Ljk5OTRDMTg4LjQgNDAuNDk5NCAxODguMSA0MC44OTk0IDE4Ny42IDQxLjA5OTRDMTg3LjEgNDEuMjk5NCAxODYuNiA0MS4wOTk0IDE4Ni4zIDQwLjc5OTRDMTgxLjYgMzUuMjk5NCAxNzQuMyAzMi4xOTk0IDE2Ni4zIDMyLjE5OTRDMTQ5LjIgMzIuMTk5NCAxMzUuOCA0Ni41OTk0IDEzNS44IDY0Ljk5OTRDMTM1LjggNzMuOTk5NCAxMzguOSA4Mi4yOTk0IDE0NC42IDg4LjM5OTRDMTUwLjMgOTQuNDk5NCAxNTggOTcuNzk5NCAxNjYuMyA5Ny43OTk0QzE3NC4yIDk3Ljc5OTQgMTgxLjUgOTQuNDk5NCAxODYuMyA4OC43OTk0QzE4Ni42IDg4LjM5OTQgMTg3LjIgODguMjk5NCAxODcuNiA4OC4zOTk0QzE4OC4xIDg4LjU5OTQgMTg4LjQgODguOTk5NCAxODguNCA4OS40OTk0Vjk2LjE5OTRIMjAyLjJaTTE2OS4zIDg1LjI5OTRDMTU4LjMgODUuMjk5NCAxNDkuNyA3Ni4zOTk0IDE0OS43IDY0Ljk5OTRDMTQ5LjcgNTMuNTk5NCAxNTguMyA0NC42OTk0IDE2OS4zIDQ0LjY5OTRDMTgwLjMgNDQuNjk5NCAxODguOSA1My41OTk0IDE4OC45IDY0Ljk5OTRDMTg4LjkgNzYuMzk5NCAxODAuMyA4NS4yOTk0IDE2OS4zIDg1LjI5OTRaIiBmaWxsPSIjMEIyMDI2Ii8+CjxwYXRoIGQ9Ik0yNzYgOTYuMDk5NlYzMy42OTk2SDI2Mi4zVjM5Ljk5OTZDMjYyLjMgNDAuNDk5NiAyNjIgNDAuODk5NiAyNjEuNSA0MS4wOTk2QzI2MSA0MS4yOTk2IDI2MC41IDQxLjA5OTYgMjYwLjIgNDAuNjk5NkMyNTUuNiAzNS4xOTk2IDI0OC40IDMyLjA5OTYgMjQwLjIgMzIuMDk5NkMyMjMuMSAzMi4wOTk2IDIwOS43IDQ2LjQ5OTYgMjA5LjcgNjQuODk5NkMyMDkuNyA4My4yOTk2IDIyMy4xIDk3LjY5OTYgMjQwLjIgOTcuNjk5NkMyNDguMSA5Ny42OTk2IDI1NS40IDk0LjM5OTYgMjYwLjIgODguNTk5NkMyNjAuNSA4OC4xOTk2IDI2MS4xIDg4LjA5OTYgMjYxLjUgODguMTk5NkMyNjIgODguMzk5NiAyNjIuMyA4OC43OTk2IDI2Mi4zIDg5LjI5OTZWOTYuMDk5NkgyNzZaTTI0My4zIDg1LjI5OTZDMjMyLjMgODUuMjk5NiAyMjMuNyA3Ni4zOTk2IDIyMy43IDY0Ljk5OTZDMjIzLjcgNTMuNTk5NiAyMzIuMyA0NC42OTk2IDI0My4zIDQ0LjY5OTZDMjU0LjMgNDQuNjk5NiAyNjIuOSA1My41OTk2IDI2Mi45IDY0Ljk5OTZDMjYyLjkgNzYuMzk5NiAyNTQuMyA4NS4yOTk2IDI0My4zIDg1LjI5OTZaIiBmaWxsPSIjMEIyMDI2Ii8+CjxwYXRoIGQ9Ik0zOTMuMyA5Ni4xOTk2VjMzLjY5OTZIMzc5LjZWMzkuOTk5NkMzNzkuNiA0MC40OTk2IDM3OS4zIDQwLjg5OTYgMzc4LjggNDEuMDk5NkMzNzguMyA0MS4yOTk2IDM3Ny44IDQxLjA5OTYgMzc3LjUgNDAuNjk5NkMzNzIuOSAzNS4xOTk2IDM2NS43IDMyLjA5OTYgMzU3LjUgMzIuMDk5NkMzNDAuMyAzMi4wOTk2IDMyNyA0Ni40OTk2IDMyNyA2NC45OTk2QzMyNyA4My40OTk2IDM0MC40IDk3Ljc5OTYgMzU3LjUgOTcuNzk5NkMzNjUuNCA5Ny43OTk2IDM3Mi43IDk0LjQ5OTYgMzc3LjUgODguNjk5NkMzNzcuOCA4OC4yOTk2IDM3OC40IDg4LjE5OTYgMzc4LjggODguMjk5NkMzNzkuMyA4OC40OTk2IDM3OS42IDg4Ljg5OTYgMzc5LjYgODkuMzk5NlY5Ni4xOTk2SDM5My4zWk0zNjAuNiA4NS4yOTk2QzM0OS42IDg1LjI5OTYgMzQxIDc2LjM5OTYgMzQxIDY0Ljk5OTZDMzQxIDUzLjU5OTYgMzQ5LjYgNDQuNjk5NiAzNjAuNiA0NC42OTk2QzM3MS42IDQ0LjY5OTYgMzgwLjIgNTMuNTk5NiAzODAuMiA2NC45OTk2QzM4MC4yIDc2LjM5OTYgMzcxLjYgODUuMjk5NiAzNjAuNiA4NS4yOTk2WiIgZmlsbD0iIzBCMjAyNiIvPgo8cGF0aCBkPSJNNDE4LjQgODguNzk5NEM0MTguNSA4OC43OTk0IDQxOC43IDg4LjY5OTQgNDE4LjggODguNjk5NEM0MTkuMSA4OC42OTk0IDQxOS41IDg4Ljg5OTQgNDE5LjcgODkuMDk5NEM0MjQuNCA5NC41OTk0IDQzMS43IDk3LjY5OTQgNDM5LjcgOTcuNjk5NEM0NTYuOCA5Ny42OTk0IDQ3MC4yIDgzLjI5OTQgNDcwLjIgNjQuODk5NEM0NzAuMiA1NS44OTk0IDQ2Ny4xIDQ3LjU5OTQgNDYxLjQgNDEuNDk5NEM0NTUuNyAzNS4zOTk0IDQ0OCAzMi4wOTk0IDQzOS43IDMyLjA5OTRDNDMxLjggMzIuMDk5NCA0MjQuNSAzNS4zOTk0IDQxOS43IDQxLjA5OTRDNDE5LjQgNDEuNDk5NCA0MTguOSA0MS41OTk0IDQxOC40IDQxLjQ5OTRDNDE3LjkgNDEuMjk5NCA0MTcuNiA0MC44OTk0IDQxNy42IDQwLjM5OTRWNi4zOTk0MUg0MDMuOFY5Ni4xOTk0SDQxNy42Vjg5Ljg5OTRDNDE3LjYgODkuMzk5NCA0MTcuOSA4OC45OTk0IDQxOC40IDg4Ljc5OTRaTTQxNyA2NC45OTk0QzQxNyA1My41OTk0IDQyNS42IDQ0LjY5OTQgNDM2LjYgNDQuNjk5NEM0NDcuNiA0NC42OTk0IDQ1Ni4yIDUzLjU5OTQgNDU2LjIgNjQuOTk5NEM0NTYuMiA3Ni4zOTk0IDQ0Ny42IDg1LjI5OTQgNDM2LjYgODUuMjk5NEM0MjUuNiA4NS4yOTk0IDQxNyA3Ni4yOTk0IDQxNyA2NC45OTk0WiIgZmlsbD0iIzBCMjAyNiIvPgo8cGF0aCBkPSJNNTEwLjEgNDYuNDk5NEM1MTEuNCA0Ni40OTk0IDUxMi42IDQ2LjU5OTQgNTEzLjQgNDYuNzk5NFYzMi41OTk0QzUxMi45IDMyLjQ5OTQgNTEyIDMyLjM5OTQgNTExLjEgMzIuMzk5NEM1MDMuOSAzMi4zOTk0IDQ5Ny4zIDM2LjA5OTQgNDkzLjggNDEuOTk5NEM0OTMuNSA0Mi40OTk0IDQ5MyA0Mi42OTk0IDQ5Mi41IDQyLjQ5OTRDNDkyIDQyLjM5OTQgNDkxLjYgNDEuODk5NCA0OTEuNiA0MS4zOTk0VjMzLjY5OTRINDc3LjlWOTYuMjk5NEg0OTEuN1Y2OC42OTk0QzQ5MS43IDU0Ljk5OTQgNDk4LjcgNDYuNDk5NCA1MTAuMSA0Ni40OTk0WiIgZmlsbD0iIzBCMjAyNiIvPgo8cGF0aCBkPSJNNTM2LjEgMzMuNjk5Mkg1MjIuMVY5Ni4yOTkySDUzNi4xVjMzLjY5OTJaIiBmaWxsPSIjMEIyMDI2Ii8+CjxwYXRoIGQ9Ik01MjguOSA2LjQ5OTAyQzUyNC4yIDYuNDk5MDIgNTIwLjQgMTAuMjk5IDUyMC40IDE0Ljk5OUM1MjAuNCAxOS42OTkgNTI0LjIgMjMuNDk5IDUyOC45IDIzLjQ5OUM1MzMuNiAyMy40OTkgNTM3LjQgMTkuNjk5IDUzNy40IDE0Ljk5OUM1MzcuNCAxMC4yOTkgNTMzLjYgNi40OTkwMiA1MjguOSA2LjQ5OTAyWiIgZmlsbD0iIzBCMjAyNiIvPgo8cGF0aCBkPSJNNTc3LjEgMzIuMDk5NkM1NTcuOSAzMi4wOTk2IDU0NCA0NS44OTk2IDU0NCA2NC45OTk2QzU0NCA3NC4yOTk2IDU0Ny4zIDgyLjU5OTYgNTUzLjIgODguNTk5NkM1NTkuMiA5NC41OTk2IDU2Ny42IDk3Ljg5OTYgNTc3IDk3Ljg5OTZDNTg0LjggOTcuODk5NiA1OTAuOCA5Ni4zOTk2IDYwMi4yIDg3Ljk5OTZMNTk0LjMgNzkuNjk5NkM1ODguNyA4My4zOTk2IDU4My41IDg1LjE5OTYgNTc4LjQgODUuMTk5NkM1NjYuOCA4NS4xOTk2IDU1OC4xIDc2LjQ5OTYgNTU4LjEgNjQuOTk5NkM1NTguMSA1My40OTk2IDU2Ni44IDQ0Ljc5OTYgNTc4LjQgNDQuNzk5NkM1ODMuOSA0NC43OTk2IDU4OSA0Ni41OTk2IDU5NC4xIDUwLjI5OTZMNjAyLjkgNDEuOTk5NkM1OTIuNiAzMy4xOTk2IDU4My4zIDMyLjA5OTYgNTc3LjEgMzIuMDk5NloiIGZpbGw9IiMwQjIwMjYiLz4KPHBhdGggZD0iTTYyNi41IDY4LjY5OUM2MjYuNyA2OC40OTkgNjI3IDY4LjM5OSA2MjcuMyA2OC4zOTlINjI3LjRDNjI3LjcgNjguMzk5IDYyOCA2OC41OTkgNjI4LjMgNjguNzk5TDY1MC40IDk2LjE5OUg2NjcuNEw2MzguOCA2MS41OTlDNjM4LjQgNjEuMDk5IDYzOC40IDYwLjM5OSA2MzguOSA1OS45OTlMNjY1LjIgMzMuNjk5SDY0OC4zTDYyNS42IDU2LjQ5OUM2MjUuMyA1Ni43OTkgNjI0LjggNTYuODk5IDYyNC4zIDU2Ljc5OUM2MjMuOSA1Ni41OTkgNjIzLjYgNTYuMTk5IDYyMy42IDU1LjY5OVY2LjQ5OTAySDYwOS43Vjk2LjI5OUg2MjMuNVY3MS44OTlDNjIzLjUgNzEuNTk5IDYyMy42IDcxLjE5OSA2MjMuOSA3MC45OTlMNjI2LjUgNjguNjk5WiIgZmlsbD0iIzBCMjAyNiIvPgo8cGF0aCBkPSJNNjg5LjkgOTcuNzk5QzcwMS4yIDk3Ljc5OSA3MTIuNyA5MC44OTkgNzEyLjcgNzcuNzk5QzcxMi43IDY5LjE5OSA3MDcuMyA2My4yOTkgNjk2LjMgNTkuNjk5TDY4OC44IDU3LjE5OUM2ODMuNyA1NS40OTkgNjgxLjMgNTMuMDk5IDY4MS4zIDQ5Ljc5OUM2ODEuMyA0NS45OTkgNjg0LjcgNDMuMzk5IDY4OS41IDQzLjM5OUM2OTQuMSA0My4zOTkgNjk4LjIgNDYuMzk5IDcwMC44IDUxLjU5OUw3MTEuOSA0NS41OTlDNzA3LjggMzcuMTk5IDY5OS4zIDMxLjk5OSA2ODkuNSAzMS45OTlDNjc3LjEgMzEuOTk5IDY2OC4xIDM5Ljk5OSA2NjguMSA1MC44OTlDNjY4LjEgNTkuNTk5IDY3My4zIDY1LjM5OSA2ODQgNjguNzk5TDY5MS43IDcxLjI5OUM2OTcuMSA3Mi45OTkgNjk5LjQgNzUuMTk5IDY5OS40IDc4LjY5OUM2OTkuNCA4My45OTkgNjk0LjUgODUuODk5IDY5MC4zIDg1Ljg5OUM2ODQuNyA4NS44OTkgNjc5LjcgODIuMjk5IDY3Ny4zIDc2LjM5OUw2NjYgODIuMzk5QzY2OS43IDkxLjg5OSA2NzguOCA5Ny43OTkgNjg5LjkgOTcuNzk5WiIgZmlsbD0iIzBCMjAyNiIvPgo8cGF0aCBkPSJNMzE0LjQgOTcuMTk5NEMzMTguOCA5Ny4xOTk0IDMyMi43IDk2Ljc5OTQgMzI0LjkgOTYuNDk5NFY4NC40OTk0QzMyMy4xIDg0LjY5OTQgMzE5LjkgODQuODk5NCAzMTggODQuODk5NEMzMTIuNCA4NC44OTk0IDMwOC4xIDgzLjg5OTQgMzA4LjEgNzEuNzk5NFY0Ni4wOTk0QzMwOC4xIDQ1LjM5OTQgMzA4LjYgNDQuODk5NCAzMDkuMyA0NC44OTk0SDMyMi44VjMzLjU5OTRIMzA5LjNDMzA4LjYgMzMuNTk5NCAzMDguMSAzMy4wOTk0IDMwOC4xIDMyLjM5OTRWMTQuMzk5NEgyOTQuM1YzMi40OTk0QzI5NC4zIDMzLjE5OTQgMjkzLjggMzMuNjk5NCAyOTMuMSAzMy42OTk0SDI4My41VjQ0Ljk5OTRIMjkzLjFDMjkzLjggNDQuOTk5NCAyOTQuMyA0NS40OTk0IDI5NC4zIDQ2LjE5OTRWNzUuMjk5NEMyOTQuMyA5Ny4xOTk0IDMwOC45IDk3LjE5OTQgMzE0LjQgOTcuMTk5NFoiIGZpbGw9IiMwQjIwMjYiLz4KPC9nPgo8ZGVmcz4KPGNsaXBQYXRoIGlkPSJjbGlwMF8xOTg0XzczMyI+CjxyZWN0IHdpZHRoPSI3MTIuOCIgaGVpZ2h0PSIxMTMiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==" alt="Databricks" height="32">
# MAGIC   <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMxIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDUzMSAyMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik04MS43OTA2IDE1OS43ODlDNzUuMDI0MiAxNTkuNzg5IDY5LjUzODkgMTY2LjU5OSA2OS41Mzg5IDE3NUgxMjYuMzY4QzEyNi4zNjggMTY2LjU5OSAxMjAuODgyIDE1OS43ODkgMTE0LjExNiAxNTkuNzg5SDgxLjc5MDZaIiBmaWxsPSIjRkY1RjQ2Ii8+CjxwYXRoIGQ9Ik0xNzkuNjE0IDgwLjc4NzFDMTY3LjUyNSAxMDAuMjA4IDE0OS4zNzUgMTI2LjkzMyAxNDEuMjcxIDEzMy43OUMxMzMuMTY3IDE0MC42NDcgMTIxLjE0OSAxNTMuMDA5IDkzLjI5MDQgMTUzLjAwOUM3My43NzM4IDE1My4wMDkgNTYuOTg2IDE0MC40NzQgNDkuNTM0OCAxMjIuNDk4QzQ5LjUzNSAxMjIuNTE5IDQ5LjUzNTMgMTIyLjU0IDQ5LjUzNTUgMTIyLjU2MUM0OC40Nzk2IDExOS45MzggNDUuOTEyOCAxMTguMDg1IDQyLjkxMTcgMTE4LjA4NUMzOC45Njg2IDExOC4wODUgMzUuNzcxOCAxMjEuMjgyIDM1Ljc3MTggMTI1LjIyNUMzNS43NzE5IDEyNi4xNSAzNS45NDggMTI2Ljk5NyAzNi4yNjg2IDEyNy43NTJDMzcuOTgzNyAxMzEuNzkzIDQyLjU0NjYgMTMxLjk2NSA0Mi41NDY2IDE0NC41NjlDNDIuNTQ2NSAxNDYuNDA0IDQyLjU0NjYgMTQzLjEwMyA0Mi41NDY2IDE0NC41NjlDMzAuNjk0MyAxNDQuNTY5IDIxLjA4NjIgMTM0Ljk2IDIxLjA4NTkgMTIzLjEwOEMyMS4wODU5IDExMS4yNTYgMzAuNjk0MiAxMDEuNjQ3IDQyLjU0NjYgMTAxLjY0N0g0NS40MjQ2VjEwMS42NDRINzkuNTE1QzgyLjA2MTcgMTAxLjY0NCA4NC41MDYzIDEwMi43MjIgODYuMDk3NSAxMDQuNzFDODguODg1MiAxMDguMTk0IDkxLjAyMTggMTExLjQzOCA5Mi41OTY2IDExNC4xMTRDOTQuMDU1NiAxMTYuNTk0IDk4LjQyNTEgMTE2LjYxOCA5OS44Njk1IDExNC4xM0MxMDEuMzkzIDExMS41MDYgMTAzLjQxNSAxMDguMzM3IDEwNS45OCAxMDQuOTI5QzEwNy41NzIgMTAyLjgxMyAxMTAuMTAzIDEwMS42NDQgMTEyLjc1MSAxMDEuNjQ0SDEyNS40MjdDMTQzLjk1MSAxMDEuNjQ0IDE1NC4xMDQgOTIuNzYyMyAxNTkuMjg5IDg2LjM2MTJDMTYxLjk3MiA4My4wNDkgMTY1Ljc4MiA4MC43ODcxIDE3MC4wNDUgODAuNzg3MUgxNzkuNjE0WiIgZmlsbD0iI0ZBQkZCQSIvPgo8cGF0aCBkPSJNOTYuMzgzOSAxMTEuNzY3Qzk2LjM4MzcgODcuODYyNiA3Ny4zMTg5IDY4LjQ3MzYgNTMuNzY3NiA2OC4zODQxQzc3LjMxOTEgNjguMjk0NyA5Ni4zODQxIDQ4LjkwNDYgOTYuMzg0MSAyNC45OTk4Qzk2LjM4NDEgMjQuOTk5NyA5Ni4zODQxIDI0Ljk5OTggOTYuMzg0MSAyNC45OTk4Qzk2LjM4NDEgNDguOTYgMTE1LjUzOCA2OC4zODM2IDEzOS4xNjUgNjguMzgzNkMxMTUuNTM4IDY4LjM4MzYgOTYuMzg0IDg3LjgwNzIgOTYuMzgzOSAxMTEuNzY3WiIgZmlsbD0iI0ZGNUY0NiIvPgo8cGF0aCBkPSJNMjczLjUxIDEzOC44MjVDMjY2LjIyNCAxMzguODI1IDI1OS44MjEgMTM3LjE2OSAyNTQuMzAxIDEzMy44NTdDMjQ4Ljg1NCAxMzAuNTQ1IDI0NC42MjIgMTI1Ljk0NSAyNDEuNjA1IDEyMC4wNTdDMjM4LjU4NyAxMTQuMDk1IDIzNy4wNzggMTA3LjE0IDIzNy4wNzggOTkuMTkxMkMyMzcuMDc4IDkxLjMxNiAyMzguNjI0IDg0LjM2MDggMjQxLjcxNSA3OC4zMjU2QzI0NC44MDYgNzIuMjE2OCAyNDkuMjIyIDY3LjQ2OTYgMjU0Ljk2MyA2NC4wODRDMjYwLjc3OCA2MC42MjQ4IDI2Ny42NTkgNTguODk1MiAyNzUuNjA4IDU4Ljg5NTJDMjg0LjU4NyA1OC44OTUyIDI5Mi4wMjEgNjEuMDY2NCAyOTcuOTA5IDY1LjQwODhDMzAzLjg3IDY5LjY3NzYgMzA3LjczNCA3NS42MzkyIDMwOS41MDEgODMuMjkzNkgyOTQuNTk3QzI5My40OTMgNzkuNDY2NCAyOTEuMzIyIDc2LjQ4NTYgMjg4LjA4MyA3NC4zNTEyQzI4NC44NDUgNzIuMjE2OCAyODAuNjUgNzEuMTQ5NiAyNzUuNDk4IDcxLjE0OTZDMjcwLjI3MiA3MS4xNDk2IDI2NS43ODIgNzIuMjkwNCAyNjIuMDI5IDc0LjU3MkMyNTguMzQ5IDc2Ljc4IDI1NS41MTUgODAuMDE4NCAyNTMuNTI4IDg0LjI4NzJDMjUxLjYxNCA4OC40ODI0IDI1MC42NTggOTMuNDg3MiAyNTAuNjU4IDk5LjMwMTZDMjUwLjY1OCAxMDUuMTE2IDI1MS42MTQgMTEwLjEyMSAyNTMuNTI4IDExNC4zMTZDMjU1LjUxNSAxMTguNTExIDI1OC4zMTIgMTIxLjcxMyAyNjEuOTE4IDEyMy45MjFDMjY1LjUyNSAxMjYuMDU1IDI2OS43NTcgMTI3LjEyMiAyNzQuNjE0IDEyNy4xMjJDMjgxLjgyNyAxMjcuMTIyIDI4Ny4yNzQgMTI1LjA5OCAyOTAuOTU0IDEyMS4wNUMyOTQuNjM0IDExNy4wMDIgMjk2LjgwNSAxMTEuNzQgMjk3LjQ2NyAxMDUuMjYzSDI3Ny40ODVWOTUuMjE2OEgzMTAuODI2VjEzNy41SDI5OC42ODJMMjk3LjU3OCAxMjYuOTAyQzI5NS44ODUgMTI5LjQwNCAyOTMuOTM0IDEzMS41NzUgMjkxLjcyNiAxMzMuNDE1QzI4OS41MTggMTM1LjE4MiAyODYuOTA2IDEzNi41NDMgMjgzLjg4OCAxMzcuNUMyODAuOTQ0IDEzOC4zODMgMjc3LjQ4NSAxMzguODI1IDI3My41MSAxMzguODI1Wk0zNDcuNDE5IDEzOC44MjVDMzQxLjg5OSAxMzguODI1IDMzNy4wNDEgMTM3LjY0NyAzMzIuODQ2IDEzNS4yOTJDMzI4LjY1MSAxMzIuODYzIDMyNS4zNzYgMTI5LjQ3OCAzMjMuMDIgMTI1LjEzNUMzMjAuNjY1IDEyMC43OTMgMzE5LjQ4OCAxMTUuNzg4IDMxOS40ODggMTEwLjEyMUMzMTkuNDg4IDEwNC4yMzMgMzIwLjYyOCA5OS4wODA4IDMyMi45MSA5NC42NjQ4QzMyNS4yNjUgOTAuMjQ4OCAzMjguNTQgODYuNzg5NiAzMzIuNzM2IDg0LjI4NzJDMzM3LjAwNCA4MS43ODQ4IDM0MS45MzYgODAuNTMzNiAzNDcuNTI5IDgwLjUzMzZDMzUyLjk3NiA4MC41MzM2IDM1Ny43MjMgODEuNzQ4IDM2MS43NzEgODQuMTc2OEMzNjUuODE5IDg2LjYwNTYgMzY4Ljk0NyA4OS44ODA4IDM3MS4xNTUgOTQuMDAyNEMzNzMuMzYzIDk4LjA1MDQgMzc0LjQ2NyAxMDIuNjE0IDM3NC40NjcgMTA3LjY5MkMzNzQuNDY3IDEwOC40MjggMzc0LjQ2NyAxMDkuMjM4IDM3NC40NjcgMTEwLjEyMUMzNzQuNDY3IDExMS4wMDQgMzc0LjM5MyAxMTEuOTI0IDM3NC4yNDYgMTEyLjg4MUgzMjguOTgyVjEwNC4zOEgzNjEuMTA4QzM2MC45NjEgMTAwLjMzMiAzNTkuNiA5Ny4xNjcyIDM1Ny4wMjQgOTQuODg1NkMzNTQuNDQ4IDkyLjUzMDQgMzUxLjI0NiA5MS4zNTI4IDM0Ny40MTkgOTEuMzUyOEMzNDQuNjk2IDkxLjM1MjggMzQyLjE5MyA5MS45Nzg0IDMzOS45MTIgOTMuMjI5NkMzMzcuNjMgOTQuNDgwOCAzMzUuODI3IDk2LjM1NzYgMzM0LjUwMiA5OC44NkMzMzMuMTc3IDEwMS4yODkgMzMyLjUxNSAxMDQuMzggMzMyLjUxNSAxMDguMTM0VjExMS4zMzVDMzMyLjUxNSAxMTQuNzk0IDMzMy4xNCAxMTcuNzc1IDMzNC4zOTIgMTIwLjI3OEMzMzUuNzE2IDEyMi43OCAzMzcuNDgzIDEyNC42OTQgMzM5LjY5MSAxMjYuMDE4QzM0MS45NzIgMTI3LjI3IDM0NC41MTIgMTI3Ljg5NSAzNDcuMzA4IDEyNy44OTVDMzUwLjQgMTI3Ljg5NSAzNTIuOTM5IDEyNy4yMzMgMzU0LjkyNiAxMjUuOTA4QzM1Ni45ODcgMTI0LjU4MyAzNTguNDk2IDEyMi44MTcgMzU5LjQ1MiAxMjAuNjA5SDM3Mi45MjFDMzcxLjg5MSAxMjQuMDY4IDM3MC4xOTggMTI3LjE5NiAzNjcuODQzIDEyOS45OTNDMzY1LjQ4OCAxMzIuNzE2IDM2Mi41OCAxMzQuODg3IDM1OS4xMjEgMTM2LjUwNkMzNTUuNjYyIDEzOC4wNTIgMzUxLjc2MSAxMzguODI1IDM0Ny40MTkgMTM4LjgyNVpNMzgzLjM4NyAxMzcuNVY4MS44NTg0SDM5NS4wODlMMzk2LjA4MyA5MS4xMzJDMzk3Ljc3NiA4Ny44OTM2IDQwMC4yMDQgODUuMzE3NiA0MDMuMzY5IDgzLjQwNEM0MDYuNTM0IDgxLjQ5MDQgNDEwLjI4OCA4MC41MzM2IDQxNC42MyA4MC41MzM2QzQxOS4xMiA4MC41MzM2IDQyMi45NDcgODEuNDkwNCA0MjYuMTEyIDgzLjQwNEM0MjkuMjc2IDg1LjI0NCA0MzEuNzA1IDg3Ljk2NzIgNDMzLjM5OCA5MS41NzM2QzQzNS4xNjQgOTUuMTggNDM2LjA0OCA5OS42Njk2IDQzNi4wNDggMTA1LjA0MlYxMzcuNUg0MjIuOFYxMDYuMjU3QzQyMi44IDEwMS42MiA0MjEuNzY5IDk4LjA1MDQgNDE5LjcwOCA5NS41NDhDNDE3LjY0OCA5My4wNDU2IDQxNC41OTMgOTEuNzk0NCA0MTAuNTQ1IDkxLjc5NDRDNDA3Ljg5NiA5MS43OTQ0IDQwNS41MDQgOTIuNDIgNDAzLjM2OSA5My42NzEyQzQwMS4zMDggOTQuOTIyNCAzOTkuNjUyIDk2Ljc2MjQgMzk4LjQwMSA5OS4xOTEyQzM5Ny4yMjQgMTAxLjU0NiAzOTYuNjM1IDEwNC40MTcgMzk2LjYzNSAxMDcuODAyVjEzNy41SDM4My4zODdaTTQ0Ny4yNTUgMTM3LjVWODEuODU4NEg0NjAuNTAzVjEzNy41SDQ0Ny4yNTVaTTQ1My44NzkgNzMuMDI2NEM0NTEuNDUgNzMuMDI2NCA0NDkuNDI2IDcyLjI5MDQgNDQ3LjgwNyA3MC44MTg0QzQ0Ni4yNjEgNjkuMjcyOCA0NDUuNDg5IDY3LjM5NiA0NDUuNDg5IDY1LjE4OEM0NDUuNDg5IDYyLjkwNjQgNDQ2LjI2MSA2MS4wNjY0IDQ0Ny44MDcgNTkuNjY4QzQ0OS40MjYgNTguMTk2IDQ1MS40NSA1Ny40NiA0NTMuODc5IDU3LjQ2QzQ1Ni4zMDggNTcuNDYgNDU4LjI5NSA1OC4xOTYgNDU5Ljg0MSA1OS42NjhDNDYxLjQ2IDYxLjA2NjQgNDYyLjI2OSA2Mi45MDY0IDQ2Mi4yNjkgNjUuMTg4QzQ2Mi4yNjkgNjcuMzk2IDQ2MS40NiA2OS4yNzI4IDQ1OS44NDEgNzAuODE4NEM0NTguMjk1IDcyLjI5MDQgNDU2LjMwOCA3My4wMjY0IDQ1My44NzkgNzMuMDI2NFpNNDk4LjU1NSAxMzguODI1QzQ5My4wMzUgMTM4LjgyNSA0ODguMTc3IDEzNy42NDcgNDgzLjk4MiAxMzUuMjkyQzQ3OS43ODcgMTMyLjg2MyA0NzYuNTEyIDEyOS40NzggNDc0LjE1NiAxMjUuMTM1QzQ3MS44MDEgMTIwLjc5MyA0NzAuNjI0IDExNS43ODggNDcwLjYyNCAxMTAuMTIxQzQ3MC42MjQgMTA0LjIzMyA0NzEuNzY0IDk5LjA4MDggNDc0LjA0NiA5NC42NjQ4QzQ3Ni40MDEgOTAuMjQ4OCA0NzkuNjc2IDg2Ljc4OTYgNDgzLjg3MiA4NC4yODcyQzQ4OC4xNCA4MS43ODQ4IDQ5My4wNzIgODAuNTMzNiA0OTguNjY1IDgwLjUzMzZDNTA0LjExMiA4MC41MzM2IDUwOC44NTkgODEuNzQ4IDUxMi45MDcgODQuMTc2OEM1MTYuOTU1IDg2LjYwNTYgNTIwLjA4MyA4OS44ODA4IDUyMi4yOTEgOTQuMDAyNEM1MjQuNDk5IDk4LjA1MDQgNTI1LjYwMyAxMDIuNjE0IDUyNS42MDMgMTA3LjY5MkM1MjUuNjAzIDEwOC40MjggNTI1LjYwMyAxMDkuMjM4IDUyNS42MDMgMTEwLjEyMUM1MjUuNjAzIDExMS4wMDQgNTI1LjUyOSAxMTEuOTI0IDUyNS4zODIgMTEyLjg4MUg0ODAuMTE4VjEwNC4zOEg1MTIuMjQ0QzUxMi4wOTcgMTAwLjMzMiA1MTAuNzM2IDk3LjE2NzIgNTA4LjE2IDk0Ljg4NTZDNTA1LjU4NCA5Mi41MzA0IDUwMi4zODIgOTEuMzUyOCA0OTguNTU1IDkxLjM1MjhDNDk1LjgzMiA5MS4zNTI4IDQ5My4zMjkgOTEuOTc4NCA0OTEuMDQ4IDkzLjIyOTZDNDg4Ljc2NiA5NC40ODA4IDQ4Ni45NjMgOTYuMzU3NiA0ODUuNjM4IDk4Ljg2QzQ4NC4zMTMgMTAxLjI4OSA0ODMuNjUxIDEwNC4zOCA0ODMuNjUxIDEwOC4xMzRWMTExLjMzNUM0ODMuNjUxIDExNC43OTQgNDg0LjI3NiAxMTcuNzc1IDQ4NS41MjggMTIwLjI3OEM0ODYuODUyIDEyMi43OCA0ODguNjE5IDEyNC42OTQgNDkwLjgyNyAxMjYuMDE4QzQ5My4xMDggMTI3LjI3IDQ5NS42NDggMTI3Ljg5NSA0OTguNDQ0IDEyNy44OTVDNTAxLjUzNiAxMjcuODk1IDUwNC4wNzUgMTI3LjIzMyA1MDYuMDYyIDEyNS45MDhDNTA4LjEyMyAxMjQuNTgzIDUwOS42MzIgMTIyLjgxNyA1MTAuNTg4IDEyMC42MDlINTI0LjA1N0M1MjMuMDI3IDEyNC4wNjggNTIxLjMzNCAxMjcuMTk2IDUxOC45NzkgMTI5Ljk5M0M1MTYuNjI0IDEzMi43MTYgNTEzLjcxNiAxMzQuODg3IDUxMC4yNTcgMTM2LjUwNkM1MDYuNzk4IDEzOC4wNTIgNTAyLjg5NyAxMzguODI1IDQ5OC41NTUgMTM4LjgyNVoiIGZpbGw9IiMxQjMxMzkiLz4KPC9zdmc+Cg==" alt="Genie" height="48">
# MAGIC </div>
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
