from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pathlib import Path


OUT_DIR = Path("data/raw_pdfs")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def create_invoice(filename, rechnungsnr, datum, lieferant, netto, mwst, brutto):
    path = OUT_DIR / filename
    c = canvas.Canvas(str(path), pagesize=A4)

    width, height = A4

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 80, lieferant)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 130, "RECHNUNG")

    c.setFont("Helvetica", 11)
    c.drawString(50, height - 170, f"Rechnungsnummer: {rechnungsnr}")
    c.drawString(50, height - 190, f"Datum: {datum}")

    c.drawString(50, height - 240, f"Netto:   {netto} EUR")
    c.drawString(50, height - 260, f"MwSt:    {mwst} EUR")
    c.drawString(50, height - 280, f"Brutto:  {brutto} EUR")

    c.save()
    print(f"Создан: {path}")


rechnungen = [
    {"filename": "invoice_01.pdf", "rechnungsnr": "RE-2026-1001", "datum": "15.07.2026", "lieferant": "Bauer Bürobedarf GmbH",            "netto": "100,00",  "mwst": "19,00",  "brutto": "119,00"},
    {"filename": "invoice_02.pdf", "rechnungsnr": "RE-2026-1002", "datum": "22.6.26",    "lieferant": "Nordwind Logistik GmbH & Co. KG",  "netto": "3128,02", "mwst": "594,32", "brutto": "3722,34"},
    {"filename": "invoice_03.pdf", "rechnungsnr": "INV-2026-1003","datum": "03.02.2026", "lieferant": "IT-Service Krüger e.K.",            "netto": "540,00",  "mwst": "102,60", "brutto": "642,60"},
    {"filename": "invoice_04.pdf", "rechnungsnr": "R-2026-1004",  "datum": "23.5.26",    "lieferant": "GreenLine Facility GmbH",          "netto": "890,50",  "mwst": "62,34",  "brutto": "952,84"},
    {"filename": "invoice_05.pdf", "rechnungsnr": "RE-2026-1005", "datum": "23.4.26",    "lieferant": "Schmidt & Partner Consulting GmbH", "netto": "2100,00", "mwst": "399,00", "brutto": "2499,00"},
    {"filename": "invoice_06.pdf", "rechnungsnr": "INV-2026-1006","datum": "13.1.26",    "lieferant": "Bauer Bürobedarf GmbH",            "netto": "75,80",   "mwst": "14,40",  "brutto": "90,20"},
    {"filename": "invoice_07.pdf", "rechnungsnr": "RE-2026-1007", "datum": "15. Mai 2026","lieferant": "Nordwind Logistik GmbH & Co. KG", "netto": "430,00",  "mwst": "81,70",  "brutto": "511,70"},
    {"filename": "invoice_08.pdf", "rechnungsnr": "R-2026-1008",  "datum": "20.07.2026", "lieferant": "IT-Service Krüger e.K.",           "netto": "1200,00", "mwst": "228,00", "brutto": "1428,00"},
    {"filename": "invoice_09.pdf", "rechnungsnr": "RE-2026-1009", "datum": "08.07.2026", "lieferant": "GreenLine Facility GmbH",          "netto": "310,75",  "mwst": "59,04",  "brutto": "369,79"},
    {"filename": "invoice_10.pdf", "rechnungsnr": "INV-2026-1010","datum": "15.6.26",    "lieferant": "Schmidt & Partner Consulting GmbH", "netto": "980,00",  "mwst": "186,20", "brutto": "1166,20"},
    {"filename": "invoice_11.pdf", "rechnungsnr": "RE-2026-1011", "datum": "9. Juni 2026","lieferant": "Bauer Bürobedarf GmbH",           "netto": "255,00",  "mwst": "48,45",  "brutto": "303,45"},
    {"filename": "invoice_12.pdf", "rechnungsnr": "R-2026-1012",  "datum": "24. Februar 2026","lieferant": "Nordwind Logistik GmbH & Co. KG","netto": "670,00","mwst": "127,30","brutto": "797,30"},
    {"filename": "invoice_13.pdf", "rechnungsnr": "INV-2026-1013","datum": "08.06.2026", "lieferant": "IT-Service Krüger e.K.",           "netto": "1875,00", "mwst": "356,25", "brutto": "2231,25"},
    {"filename": "invoice_14.pdf", "rechnungsnr": "RE-2026-1014", "datum": "9. Januar 2026","lieferant": "GreenLine Facility GmbH",       "netto": "490,00",  "mwst": "34,30",  "brutto": "524,30"},
    {"filename": "invoice_15.pdf", "rechnungsnr": "R-2026-1015",  "datum": "21. April 2026","lieferant": "Schmidt & Partner Consulting GmbH","netto": "3200,00","mwst": "608,00","brutto": "3808,00"},
]

for r in rechnungen:
    create_invoice(**r)