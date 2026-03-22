import pandas as pd

def reconcile_data(df1: pd.DataFrame, df2: pd.DataFrame):
    
    # Merge both datasets on transaction_id
    merged = df1.merge(df2, on="transaction_id", how="outer", suffixes=("_sys1", "_sys2"), indicator=True)

    # Matched transactions
    matched = merged[(merged["_merge"] == "both") & (merged["amount_sys1"] == merged["amount_sys2"]) & (merged["status_sys1"] == merged["status_sys2"])]

    # Amount mismatch
    amount_mismatch = merged[(merged["_merge"] == "both") & (merged["amount_sys1"] != merged["amount_sys2"])]

    # Status mismatch
    status_mismatch = merged[(merged["_merge"] == "both") & (merged["status_sys1"] != merged["status_sys2"])]

    # Missing in system1
    missing_in_sys1 = merged[merged["_merge"] == "right_only"]

    # Missing in system2
    missing_in_sys2 = merged[merged["_merge"] == "left_only"]

    return {
        "matched": matched,
        "amount_mismatch": amount_mismatch,
        "status_mismatch": status_mismatch,
        "missing_in_sys1": missing_in_sys1,
        "missing_in_sys2": missing_in_sys2
    }