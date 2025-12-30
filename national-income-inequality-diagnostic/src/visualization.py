import matplotlib.pyplot as plt

def plot_germany_trend(df, save_path=None):
    plt.figure(figsize=(10,5))
    plt.plot(df["year"], df["gini"])
    plt.title("Income Inequality Trend in Germany")
    plt.xlabel("Year")
    plt.ylabel("Gini Index")
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
