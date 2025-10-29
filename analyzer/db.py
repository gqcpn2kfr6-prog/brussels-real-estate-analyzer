import os
import duckdb
from pathlib import Path

DB_PATH = Path("data/realestate.duckdb")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

con = duckdb.connect(str(DB_PATH))

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS listings (
    id VARCHAR PRIMARY KEY,
    source VARCHAR,
    title VARCHAR,
    price DOUBLE,
    currency VARCHAR,
    city VARCHAR,
    commune VARCHAR,
    district VARCHAR,
    address VARCHAR,
    rooms INTEGER,
    bedrooms INTEGER,
    bathrooms INTEGER,
    area DOUBLE,
    floor INTEGER,
    type VARCHAR,
    url VARCHAR,
    created_at TIMESTAMP DEFAULT now(),
    fetched_at TIMESTAMP DEFAULT now()
);
"""
con.execute(SCHEMA_SQL)
