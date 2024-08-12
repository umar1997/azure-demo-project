import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_CONNECTION_STRING")
app.config['SECRET_KEY'] = 'k8icNo2oJ+V^XeQjFgzN963qmm'