import sqlite3

conn = sqlite3.connect("incidents.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents(
id INTEGER PRIMARY KEY,
location TEXT,
event TEXT,
timestamp TEXT
)
""")

conn.commit()

def store_incident(location, event, timestamp):

    cursor.execute(
        "INSERT INTO incidents(location,event,timestamp) VALUES(?,?,?)",
        (location, event, timestamp)
    )

    conn.commit()
