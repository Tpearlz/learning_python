#Required Libraries
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL (update with your credentials)
db_user = "postgres"
db_pass = "admin"
db_host = "localhost"
db_port = "5432"
db_name = "Foodr"
engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")
print("✅ Connected to the database successfully!")
