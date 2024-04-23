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

# Write a record to table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#   sql_request = " INSERT INTO courses VALUES (?,?,?,?)" # ? are placeholders
#   sqlite_conn.execute(sql_request, (251, "Intro to Python", 100, 30)) # pass tuples for values
#   sqlite_conn.commit() # run the requests


# add multiple records  to the table.
# courses = [
#   (252, "Intro to JavaScript", 100, 30),
#   (351, "Understanding Algorithms", 50, 25),
#   (773, "Getting to Know Node.js", 75, 50),
#   (101, "How to Rubber Duck", 5, 90)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#   sql_request = " INSERT INTO courses VALUES (?,?,?,?)" # ? are placeholders
#   for course in courses:
#     sqlite_conn.execute(sql_request, course)
#   sqlite_conn.commit() # run the requests

# Reading data from the database.
with sqlite3.connect(DB_NAME) as sqlite_conn:
  sql_request = "SELECT * FROM courses WHERE reviews_qrt>30"
  sql_cursor = sqlite_conn.execute(sql_request)
  # for record in sql_cursor: # can unpack
  #   id, title, student_qty, review_qty = record
  #   print(record)
  #   print(id)

  records = sql_cursor.fetchall() # returns EVERYTHING
  print(records)