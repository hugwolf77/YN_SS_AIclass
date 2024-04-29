import pandas as pd
import sqlite3
from DW.DB.async_connection import get_db, conn_db


df = pd.read_excel('./DW/storage/test_keystats_01.xlsx')
print(f"df : {df.head()}")

db_con = conn_db()
print(db_con)
table_name = 'economic_idx100'
if_exists = 'replace'

with db_con.connect() as con:
 df.to_sql(
    name=table_name.lower(),
    con=con,
    if_exists=if_exists
    )