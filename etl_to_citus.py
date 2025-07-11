<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
from sqlalchemy import create_engine, text

# Koneksi ke Citus Coordinator
db_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/analytics'
engine = create_engine(db_url)

# Load CSV
df = pd.read_csv('sales_data.csv')

# Buat tabel dan distribusikan
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS sales"))
    conn.execute(text("""
        CREATE TABLE sales (
            sale_id   INT,
            region    TEXT,
            product   TEXT,
            amount    NUMERIC,
            sale_date DATE,
            PRIMARY KEY (region, sale_id)
        )
    """))
    conn.commit()

    # Distribusi tabel ke worker berdasarkan kolom 'region'
    conn.execute(text("SELECT create_distributed_table('sales', 'region');"))
    conn.commit()

# Masukkan data ke tabel
df.to_sql('sales', engine, if_exists='append', index=False)

print("✅ ETL selesai, data sudah masuk ke Citus.")
=======
import pandas as pd
from sqlalchemy import create_engine, text

# Koneksi ke Citus Coordinator
db_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/analytics'
engine = create_engine(db_url)

# Load CSV
df = pd.read_csv('sales_data.csv')

# Buat tabel dan distribusikan
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS sales"))
    conn.execute(text("""
        CREATE TABLE sales (
            sale_id   INT,
            region    TEXT,
            product   TEXT,
            amount    NUMERIC,
            sale_date DATE,
            PRIMARY KEY (region, sale_id)
        )
    """))
    conn.commit()

    # Distribusi tabel ke worker berdasarkan kolom 'region'
    conn.execute(text("SELECT create_distributed_table('sales', 'region');"))
    conn.commit()

# Masukkan data ke tabel
df.to_sql('sales', engine, if_exists='append', index=False)

print("✅ ETL selesai, data sudah masuk ke Citus.")
>>>>>>> 5183ee9 (Resolve merge conflicts from pulling origin/main 1)
=======
import pandas as pd
from sqlalchemy import create_engine, text

# Koneksi ke Citus Coordinator
db_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/analytics'
engine = create_engine(db_url)

# Load CSV
df = pd.read_csv('sales_data.csv')

# Buat tabel dan distribusikan
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS sales"))
    conn.execute(text("""
        CREATE TABLE sales (
            sale_id   INT,
            region    TEXT,
            product   TEXT,
            amount    NUMERIC,
            sale_date DATE,
            PRIMARY KEY (region, sale_id)
        )
    """))
    conn.commit()

    # Distribusi tabel ke worker berdasarkan kolom 'region'
    conn.execute(text("SELECT create_distributed_table('sales', 'region');"))
    conn.commit()

# Masukkan data ke tabel
df.to_sql('sales', engine, if_exists='append', index=False)

print("✅ ETL selesai, data sudah masuk ke Citus.")
<<<<<<< HEAD
>>>>>>> bf48ce0cd31e573436ed1a1ecdcc1f026c297e9e
=======
>>>>>>> 9b45ada (Update .gitignore to exclude data folder and .env file)
>>>>>>> 5183ee9 (Resolve merge conflicts from pulling origin/main 1)
