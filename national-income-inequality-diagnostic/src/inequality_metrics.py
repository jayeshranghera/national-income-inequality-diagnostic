def region_yearly_average(df):
    return (
        df.groupby(["region", "year"])["gini"]
        .mean()
        .reset_index()
    )


def inequality_persistence(df):
    return (
        df.groupby("country")["gini"]
        .agg(["mean", "std"])
        .reset_index()
        .sort_values("mean", ascending=False)
    )