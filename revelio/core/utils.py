from numpy import random
import pandas as pd

def _read_csv(uploaded_bytes, sep=",", dec=".", encoding="utf-8"):
    from io import BytesIO
    import pandas as pd

    bio = BytesIO(uploaded_bytes)
    df = pd.read_csv(bio, sep=sep, decimal=dec, encoding=encoding)
    return df

def _read_excel(uploaded_bytes, sheet_name=None):
    from io import BytesIO
    import pandas as pd

    bio = BytesIO(uploaded_bytes)
    if sheet_name:
        df = pd.read_excel(bio, sheet_name=sheet_name)
        return df
    else:
        df = pd.ExcelFile(bio)
        
    return df

def get_dummy_text():

    return f"Hello, Reveli{'o'*random.randint(1, 200)}!"

def get_excel_sheets(path):

    with open(path, 'rb') as f:

        xls = pd.ExcelFile(f)
        
    return xls.sheet_names