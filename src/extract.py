import pdfplumber
import ollama
import json
from pathlib import Path

RAW_DIR = Path("data/raw_pdfs")

def read_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_with_llm(text):
    prompt = f"""Du bist ein Datenextraktions-Assistent. Extrahiere Daten aus dem Rechnungstext.
Gib NUR dieses JSON zurück, ohne Text davor oder danach:

{{
  "rechnungsnr": "Rechnungsnummer hier",
  "datum": "Datum hier",
  "lieferant": "Firmenname des Lieferanten hier",
  "netto": 0.00,
  "mwst": 0.00,
  "brutto": 0.00
}}

Rechnungstext:
{text}"""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response["message"]["content"]
    return json.loads(result)

# обрабатываем все файлы
pdf_files = sorted(RAW_DIR.glob("*.pdf"))
results = []

for pdf_path in pdf_files:
    print(f"Verarbeite {pdf_path.name}...")
    text = read_pdf(pdf_path)
    try:
        data = extract_with_llm(text)
        results.append({"file": pdf_path.name, "data": data})
    except:
        results.append({"file": pdf_path.name, "data": None, "error": "parsing failed"})

with open("output/extracted.json", "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Fertig! Ergebnis in output/extracted.json")