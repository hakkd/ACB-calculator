import sqlite3

conn = sqlite3.connect("acb_calculator.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users
""")
