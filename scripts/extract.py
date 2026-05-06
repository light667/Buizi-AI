import trafilatura
import os
import re
from urllib.parse import urlparse

# Liste des URLs à scraper
urls = [
    "https://www.shopify.com/blog/213396233-how-to-start-a-food-business",
    "https://www.shopify.com/blog/start-online-tshirt-business",
    "https://www.shopify.com/blog/customizing-store-theme",
    "https://www.shopify.com/blog/customer-experience-design",
    "https://www.shopify.com/blog/shopify-stores"
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