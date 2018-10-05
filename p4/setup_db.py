import sqlite3

# connect to the database. This will create the file if it doesn't exist already
conn = sqlite3.connect("songs.db")

# get a cursor object to execute SQLite statements
cur = conn.cursor()
# get rid of the table if it already exists
# this is helpful if you want to restart creating the database
cur.execute("drop table if exists songs")
# Create table with columns
cur.execute("create table songs(name text,artist text,genre text,year integer)")

# save changes and close the connection
conn.commit()
conn.close()