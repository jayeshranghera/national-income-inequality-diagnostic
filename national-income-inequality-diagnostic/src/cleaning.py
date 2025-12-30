import pandas as pd

def reshape_gini_data(df):
    df = df.rename(columns={
        "Country Name": "country",
        "Country Code": "country_code"
    })
    
    year_cols = df.columns[4:]
    
    long_df = df[["country", "country_code"] + list(year_cols)].melt(
        id_vars=["country", "country_code"],
        var_name="year",
        value_name="gini"
    )
    
    long_df["year"] = pd.to_numeric(long_df["year"], errors="coerce")
    long_df["gini"] = pd.to_numeric(long_df["gini"], errors="coerce")
    
    return long_df.dropna(subset=["gini"])


def merge_country_metadata(gini_df, meta_df):
    meta_df = meta_df[["Country Code", "Region", "IncomeGroup"]].rename(
        columns={
            "Country Code": "country_code",
            "IncomeGroup": "income_group"
        }
    )
    
    return gini_df.merge(meta_df, on="country_code", how="left")
