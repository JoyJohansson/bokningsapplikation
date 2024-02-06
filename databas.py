import secrets
from psycopg2 import connect, DatabaseError, pool
from dotenv import load_dotenv
import os

load_dotenv()

# Set up a connection pool
db_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
)

def execute_query(query, parameter=None, fetch_result=False):
    # ... (Same as in the original file)

def generate_random_token():
    return secrets.token_urlsafe()
