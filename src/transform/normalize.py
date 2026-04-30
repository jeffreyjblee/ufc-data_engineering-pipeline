import pandas as pd

def normalize_fighter_data(data):
    return pd.json_normalize(data)