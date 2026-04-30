import os


def save_to_csv(df, filename="ufc_fighterstats.csv"):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

    output_path = os.path.join(project_root, "data", "processed", filename)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)