import pandas

def clean_data(df: pandas.DataFrame) -> pandas.DataFrame:
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna()
    df['amount'] = df['amount'].astype(float)
    df['transaction_date'] = pandas.to_datetime(df['transaction_date'])
    df['status'] = df['status'].str.lower().str.strip()
    return df