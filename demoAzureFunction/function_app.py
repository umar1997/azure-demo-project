import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv

import sqlalchemy
from sqlalchemy import create_engine, func as sql_func
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

import io
import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient

load_dotenv()
Base = declarative_base()
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True)
    name = Column(String(64), nullable=False)
    email = Column(String(64), unique = True)
    email_id = Column(String(64), unique = True, index= True)
    gender = Column(String(32), nullable=False)
    age = Column(Integer, nullable=True)
    position = Column(String(64), nullable=False)
    reports_to = Column(String(64))


def insert_df_to_db(df):
    DATABASE_URL = os.getenv("POSTGRES_CONNECTION_STRING")
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        max_id = db.query(sql_func.max(User.id)).scalar()
    except Exception as e:
        max_id = 0

    try:
        for _, row in df.iterrows():
            max_id += 1
            user = User(
                id=max_id,
                name=row["Name"],
                email=row["Email"],
                email_id= row["Email"][:row["Email"].index("@")],
                gender=row["Gender"],
                age=row["Age"],
                position=row["Position"],
                reports_to=row["Reports_To"]
            )
            print(user.id,user.name, user.email, user.email_id, user.gender, user.age, user.position, user.reports_to)
            db.add(user)
        db.commit() 
        print("Data inserted successfully.")
        return "Data inserted successfully."
    except SQLAlchemyError as e:
        db.rollback() 
        return f"Custom Exception (func-insert_df_to_db): {e}"
    finally:
        db.close() 

def read_csv_to_df(blob_name):
    """
    Link: https://stackoverflow.com/questions/62670991/read-csv-from-azure-blob-storage-and-store-in-a-dataframe
    """
    container_name = os.getenv("BLOB_STORAGE_CONTAINER_NAME")
    account_name = os.getenv("BLOB_STORAGE_ACCOUNT_NAME")
    account_key = os.getenv("BLOB_STORAGE_ACCOUNT_KEY")
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
    df = pd.read_csv(f"abfs:///{container_name}/{blob_name}", storage_options={"account_name": account_name, "connection_string": connection_string})
    df['Age'] = df['Age'].replace({np.nan: None})
    return df

def delete_user(db, email_id):
    user_to_delete = db.query(User).filter(User.email_id == email_id).first()
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()


@app.route(route="teamBulkUploadTrigger")
def teamBulkUploadTrigger(req: func.HttpRequest) -> func.HttpResponse:
    # blob_name = "team.csv"
    blob_name = req.params.get('blob_name')
    df = read_csv_to_df(blob_name)
    message = insert_df_to_db(df)
    return func.HttpResponse(message)

######################### TO RUN LOCALLY
# def main():
#     df = read_csv_to_df()
#     insert_df_to_db(df)


# if __name__ == "__main__":
#     main()