import trafilatura
import os
import re
from urllib.parse import urlparse

# Liste des URLs à scraper
urls = [
    "https://contentmarketinginstitute.com/content-marketing-strategy/content-led-marketing-strategy",
    "https://contentmarketinginstitute.com/content-operations/companies-destroying-marketing-teams",
    "https://contentmarketinginstitute.com/audience-building/audiences-loyal-communities",
    "https://contentmarketinginstitute.com/content-creation-distribution/content-writing-examples-tips-tools"
]

# Dossier de sortie
output_dir = "articles"
os.makedirs(output_dir, exist_ok=True)

def clean_filename(text):
    """Nettoie le nom de fichier"""
    text = re.sub(r'[\\/*?:"<>|]', "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:100]  # limite longueur

for i, url in enumerate(urls):
    print(f"\n🔎 Traitement de : {url}")

    downloaded = trafilatura.fetch_url(url)

    if not downloaded:
        print("❌ Échec du téléchargement")
        continue

    text = trafilatura.extract(downloaded)

    if not text:
        print("❌ Échec de l'extraction")
        continue

    # Générer un nom de fichier basé sur le domaine + index
    domain = urlparse(url).netloc
    filename = f"{domain}_{i+1}.txt"
    filename = clean_filename(filename)

    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Sauvegardé dans : {filepath}")

print("\n🎉 Terminé !")