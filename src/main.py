import matplotlib.pyplot as plt
import seaborn as sns
from extract.fighter_api import get_fighter_stats
from transform.normalize import normalize_fighter_data
from load.csv_loader import save_to_csv
from config.settings import FIGHTERS, BASE_DIR

def main():
    data = []

    # EXTRACT
    for f in FIGHTERS:
        result = get_fighter_stats(f)
        if result:
            data.append(result)

    # TRANSFORM
    df = normalize_fighter_data(data)

    # LOAD
    save_to_csv(df)

    print(df)

    print(df.columns.tolist())

    # VISUALIZE
    df_sorted = df.sort_values('sig_str_landed_per_min', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 7))

    x = range(len(df_sorted))
    width = 0.35

    bars1 = ax.barh([i + width / 2 for i in x], df_sorted['sig_str_landed_per_min'],
                    width, label='Landed (Offense)', color='#8B0000')
    bars2 = ax.barh([i - width / 2 for i in x], df_sorted['sig_str_absorbed_per_min'],
                    width, label='Absorbed (Defense)', color='#CD853F')

    ax.set_yticks(list(x))
    ax.set_yticklabels(df_sorted['name'])
    ax.set_title('Offensive vs Defensive Efficiency by Fighter', fontsize=16, fontweight='bold')
    ax.set_xlabel('Significant Strikes per Minute')
    ax.legend()
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    plt.tight_layout()
    plt.savefig(BASE_DIR / 'images' / 'ufc_viz.png', dpi=150, bbox_inches='tight')
    print("Chart saved as ufc_viz.png!")

if __name__ == "__main__":
    main()