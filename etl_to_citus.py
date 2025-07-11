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
