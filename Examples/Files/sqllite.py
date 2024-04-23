import sqlite3

DB_NAME = 'sqlite_db.db'

# Create table if it doesn't exist
with sqlite3.connect(DB_NAME) as sqlite_conn:
  sql_request ="""
  CREATE TABLE IF NOT EXISTS courses (
    id integer PRIMARY KEY,
    title text NOT NULL,
    student_qty integer,
    reviews_qrt integer
  );
  """
  #run request
  sqlite_conn.execute(sql_request)

# Create db if absent
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#   print(sqlite_conn)
#   print(type(sqlite_conn))