import pandas as pd

def load_file(file_path: str) -> pd.DataFrame:
    try:
        filename = file_path.filename.lower()

        if filename.endswith(".csv"):
            return pd.read_csv(file_path.file)
        
        elif filename.endswith(".xlsx"):
            return pd.read_excel(file_path.file)
        
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(f"Error loading file {e}")
        return pd.DataFrame

