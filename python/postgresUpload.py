from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd
import os
import re

# -----------------------------
# Database Config
# -----------------------------
DB_USER = "postgres"
DB_PASSWORD = quote_plus("Yash@2003")
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crime_db"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

with engine.connect():
    print("✅ Connected to PostgreSQL")

# -----------------------------
# Helper Functions
# -----------------------------
def clean_column_name(col):
    col = col.strip().lower()
    col = re.sub(r"[^\w]+", "_", col)     # remove special chars
    col = re.sub(r"_+", "_", col)         # remove double underscores
    if col[0].isdigit():
        col = "_" + col
    return col

def preprocess_dataframe(df):
    # 1️⃣ Clean column names
    df.columns = [clean_column_name(c) for c in df.columns]

    # 2️⃣ Trim strings
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip()

    # 3️⃣ Standardize missing values
    df.replace(["", "NA", "N/A", "null", "None"], pd.NA, inplace=True)

    # 4️⃣ Convert date columns automatically
    for col in df.columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # 5️⃣ Convert numeric columns safely
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = pd.to_numeric(df[col], errors="ignore")

    return df

# -----------------------------
# CSV Folder
# -----------------------------
CSV_FOLDER = r"project\data"

# -----------------------------
# Load Pipeline
# -----------------------------
for file in os.listdir(CSV_FOLDER):
    if file.endswith(".csv"):
        file_path = os.path.join(CSV_FOLDER, file)

        table_name = clean_column_name(file.replace(".csv", ""))

        print(f"\n🚀 Processing {file} → table: {table_name}")

        df = pd.read_csv(file_path)

        df = preprocess_dataframe(df)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False,
            chunksize=10000,
            method="multi"
        )

        print(f"✅ {file} cleaned & loaded successfully")

print("\n🎉 ALL CSV FILES CLEANED, TRANSFORMED & LOADED")
