from extract.fighter_api import get_fighter_stats
from transform.normalize import normalize_fighter_data
from load.csv_loader import save_to_csv

fighters = [
    "conor-mcgregor",
    "khabib-nurmagomedov",
    "jon-jones",
    "israel-adesanya",
    "kamaru-usman",
    "georges-st-pierre",
    "max-holloway",
    "jose-aldo",
    "demetrious-johnson",
    "bj-penn",
    "daniel-cormier"
]

def main():
    data = []

    # EXTRACT
    for f in fighters:
        result = get_fighter_stats(f)
        if result:
            data.append(result)

    # TRANSFORM
    df = normalize_fighter_data(data)

    # LOAD
    save_to_csv(df)

    print(df)

if __name__ == "__main__":
    main()