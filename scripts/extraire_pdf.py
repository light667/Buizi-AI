import fitz  # PyMuPDF
import os

pdf_path = r"C:\Users\netha\Dev\projet-buizi\chap317042014MLM.pdf"

os.makedirs("articles", exist_ok=True)

# nom du fichier txt basé sur le pdf
base_name = os.path.splitext(os.path.basename(pdf_path))[0]
txt_path = os.path.join("articles", base_name + ".txt")

doc = fitz.open(pdf_path)

text = ""

for page in doc:
    text += page.get_text() + "\n"

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ PDF converti en {txt_path}")