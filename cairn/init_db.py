
import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

# Run schema script to create new tables
with open('cairn_db_schema.sql') as f:
    script = f.read()
    cur.executescript(script)

# Example data insertion for the new schema
cur.execute("INSERT INTO Users (username, email) VALUES (?, ?)", ('JohnDoe', 'johndoe@example.com'))
cur.execute("INSERT INTO Conversations (user_id) VALUES (?)", (1,))
cur.execute("INSERT INTO Messages (conversation_id, sender, message) VALUES (?, ?, ?)", (1, 'user', 'Hello, how can I get help?'))

connection.commit()
connection.close()
