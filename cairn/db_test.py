
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('database.db')

cur = connection.cursor()

# Test retrieval from the Users table
print(cur.execute("SELECT * FROM Users").fetchall())

# Test retrieval from the Conversations table
print(cur.execute("SELECT * FROM Conversations").fetchall())

# Test retrieval from the Messages table
print(cur.execute("SELECT * FROM Messages").fetchall())

connection.close()
