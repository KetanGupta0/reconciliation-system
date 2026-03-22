import pandas as pd

def generate_excel_report(result: dict, file_path: str):
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        
        for key, df in result.items():
            df.to_excel(writer, sheet_name=key, index=False)

    print(f"Report generated at {file_path}")