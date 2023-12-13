import pymysql
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect

"""

This script uses the pymysql library for connecting to MySQL, 
so you might need to install that (pip install pymysql) if you haven't already.

It also uses python-dotenv for bringing in secrets from your .env file 

The .env should have the following in it:

DB_HOST=your_host
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_PORT=3306
DB_CHARSET=utf8mb4

The default port is set to 3306 for MySQL, but you can override it by 
modifying the DB_PORT in your .env file.

The connection string is MySQL-specific, incorporating the specified port and charset.

"""

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("172.190.97.237")
DB_DATABASE = os.getenv("emr")
DB_USERNAME = os.getenv("keerthana")
DB_PASSWORD = os.getenv("keerthana2023")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)