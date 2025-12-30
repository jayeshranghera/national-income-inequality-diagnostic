import pandas as pd

def load_raw_gini_data(path):
    return pd.read_csv(path, skiprows=4)

def load_processed_data(path):
    return pd.read_csv(path)

def load_country_metadata(path):
    return pd.read_csv(path)