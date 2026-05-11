import sqlite3
import re

# Connect database
conn = sqlite3.connect("scam_jobs.db")

cursor = conn.cursor()

# Create table
cursor.execute("""

CREATE TABLE IF NOT EXISTS scans (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    job_text TEXT,

    result TEXT,

    probability INTEGER

)

""")

conn.commit()

conn.close()

print("Database Created Successfully")