import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("POSTGRES_CONNECTION_STRING")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()
result = db.execute(text("SELECT schema_name FROM information_schema.schemata;"))
tables = result.fetchall()
for table in tables: 
    print(table[0])

db.close()