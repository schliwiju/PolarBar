
import polars as pl
import matplotlib.pyplot as plt

def load_and_bin_data(filepath, bin_size=60):
    # Load data
    df = pl.read_csv(filepath)

    # Assuming the time column is called 't' and in seconds
    df = df.with_column((df['t'] / bin_size).floor().alias('bin'))

    # Count events per bin
    binned_df = df.groupby('bin').agg(pl.col('t').count().alias('count'))

    return binned_df

def plot_data(binned_df):
    plt.figure(figsize=(10, 5))
    plt.plot(binned_df['bin'] * 60, binned_df['count'], marker='o', linestyle='-')  # Convert bin number back to seconds
    plt.title('Photon Count Rate over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Count')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filepath = "data/PS1-10jh_gAperture_photons.csv"
    binned_df = load_and_bin_data(filepath)
    plot_data(binned_df)
