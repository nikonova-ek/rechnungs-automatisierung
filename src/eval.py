import json

ground_truth = {
    "invoice_01.pdf": {"rechnungsnr": "RE-2026-1001", "lieferant": "Bauer Bürobedarf GmbH", "netto": 100.0, "brutto": 119.0},
    "invoice_05.pdf": {"rechnungsnr": "RE-2026-1005", "lieferant": "Schmidt & Partner Consulting GmbH", "netto": 2100.0, "brutto": 2499.0},
    "invoice_06.pdf": {"rechnungsnr": "INV-2026-1006", "lieferant": "Bauer Bürobedarf GmbH", "netto": 75.8, "brutto": 90.2},
    "invoice_08.pdf": {"rechnungsnr": "R-2026-1008", "lieferant": "IT-Service Krüger e.K.", "netto": 1200.0, "brutto": 1428.0},
    "invoice_10.pdf": {"rechnungsnr": "INV-2026-1010", "lieferant": "Schmidt & Partner Consulting GmbH", "netto": 980.0, "brutto": 1166.2},
    "invoice_11.pdf": {"rechnungsnr": "RE-2026-1011", "lieferant": "Bauer Bürobedarf GmbH", "netto": 255.0, "brutto": 303.45},
    "invoice_12.pdf": {"rechnungsnr": "R-2026-1012", "lieferant": "Nordwind Logistik GmbH & Co. KG", "netto": 670.0, "brutto": 797.3},
    "invoice_13.pdf": {"rechnungsnr": "INV-2026-1013", "lieferant": "IT-Service Krüger e.K.", "netto": 1875.0, "brutto": 2231.25},
    "invoice_15.pdf": {"rechnungsnr": "R-2026-1015", "lieferant": "Schmidt & Partner Consulting GmbH", "netto": 3200.0, "brutto": 3808.0},
}

# Extrahierte Daten laden
with open("output/extracted.json", "r") as f:
    extracted = json.load(f)

# Nur erfolgreiche Einträge
successful = {item["file"]: item["data"] for item in extracted if item["data"] is not None}

# Felder vergleichen
fields = ["rechnungsnr", "lieferant", "netto", "brutto"]
total = 0
correct = 0

for filename, truth in ground_truth.items():
    if filename not in successful:
        continue
    extracted_data = successful[filename]
    for field in fields:
        total += 1
        truth_val = str(truth[field]).strip()
        extracted_val = str(extracted_data.get(field, "")).strip()
        if truth_val == extracted_val:
            correct += 1
        else:
            print(f"{filename} | {field}: erwartet '{truth_val}', erhalten '{extracted_val}'")

accuracy = correct / total * 100
print(f"\nGenauigkeit: {correct}/{total} Felder korrekt = {accuracy:.1f}%")