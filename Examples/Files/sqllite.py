import sqlite3

DB_NAME = 'sqlite_db.db'

# Create db if absent
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#   print(sqlite_conn)
#   print(type(sqlite_conn))

# Create table if it doesn't exist
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#   sql_request ="""
#   CREATE TABLE IF NOT EXISTS courses (
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     student_qty integer,
#     reviews_qrt integer
#   );
#   """
#   #run request
#   sqlite_conn.execute(sql_request)

# Write data to table
with sqlite3.connect(DB_NAME) as sqlite_conn:
  sql_request = " INSERT INTO courses VALUES (?,?,?,?)" # ? are placeholders
  sqlite_conn.execute(sql_request, (251, "Intro to Python", 100, 30)) # pass tuples for values
  sqlite_conn.commit() # run the requests