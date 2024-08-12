import psycopg2

import pandas as pd

conn = psycopg2.connect(database="person_db",
                        host="localhost",
                        user="umar",
                        password="umar",
                        port="5432")


query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = ''
"""

query = "SELECT * FROM person"

cursor = conn.cursor()
cursor.execute(query)


table_names = cursor.fetchall()
for table_name in table_names:
    print(table_name[0])