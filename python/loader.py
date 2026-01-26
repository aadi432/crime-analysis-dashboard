import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

# ---------- CONNECTION ----------
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB = os.getenv("MYSQL_DB")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)


# ---------- CLEANING ----------
def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    # 1) Remove duplicates
    df = df.drop_duplicates()

    # 2) Trim spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # 3) SQL friendly names
    df.columns = [
        c.lower()
         .replace(".", "")
         .replace("-", "_")
         .replace(" ", "_")
        for c in df.columns
    ]

    # 4) TYPE FIXES
    for col in df.columns:

        if "age" in col:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(df[col].median())

        # 👉 STRICT DATE PARSE TO AVOID WARNINGS
        if "date" in col or "occurrence" in col:
            df[col] = pd.to_datetime(
                df[col],
                format="%d-%m-%Y",
                dayfirst=False,
                errors="coerce"
            )

        if "gender" in col:
            df[col] = df[col].replace({
                "female": "F",
                "Female": "F",
                "male": "M",
                "Male": "M",
                "Female ": "F"
            })

    # 5) Remaining nulls
    df = df.fillna("unknown")

    return df


# ---------- LOADER ----------
def load_cleaned_csv(csv_path: str):

    try:
        file = os.path.basename(csv_path)

        # 👉 TABLE NAME FROM CSV
        table_name = file.replace(".csv", "").lower()

        print(f"Processing file: {file}")
        print(f"Target table : {table_name}")

        df = pd.read_csv(csv_path, low_memory=False)

        df = clean_dataframe(df)

        # pandas AUTO CREATE
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=2000
        )

        print(f"✅ {len(df)} rows loaded → {table_name}\n")

    except Exception as e:
        print("❌ Pipeline Failed:", csv_path, e)


# ---------- RUN ALL CSV ----------
if __name__ == "__main__":

    DATA_FOLDER = "project/data"

    if not os.path.exists(DATA_FOLDER):
        print("Data folder not found")
        exit()

    for file in os.listdir(DATA_FOLDER):

        if not file.endswith(".csv"):
            continue

        path = os.path.join(DATA_FOLDER, file)

        load_cleaned_csv(path)

    print("All CSV processed")
