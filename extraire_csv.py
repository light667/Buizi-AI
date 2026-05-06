import csv
import os

# chemin du fichier CSV
csv_path = r"C:\Users\netha\Dev\projet-buizi\marketing_campaign.csv"

# créer le dossier s'il n'existe pas
os.makedirs("articles", exist_ok=True)

# récupérer le nom du fichier sans extension
base_name = os.path.splitext(os.path.basename(csv_path))[0]

# construire le chemin du fichier txt
txt_path = os.path.join("articles", base_name + ".txt")

with open(csv_path, "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)

    with open(txt_path, "w", encoding="utf-8") as txt_file:
        for row in reader:
            line = " | ".join(row)
            txt_file.write(line + "\n")

print(f"✅ Conversion terminée dans {txt_path}")