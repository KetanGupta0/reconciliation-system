import pandas as pd

REQUIRED_COLUMNS = ["transaction_id", "amount", "transaction_date", "status"]

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # Normalize column names
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    
    return df


def validate_schema(df: pd.DataFrame):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    
    if missing:
        raise ValueError(f"Missing required columns: {missing}")