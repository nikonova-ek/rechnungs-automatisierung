import json
import pandas as pd
from pathlib import Path

# JSON-Datei laden
with open("output/extracted.json", "r") as f:
    raw = json.load(f)

# Nur erfolgreiche Einträge übernehmen
records = []
for item in raw:
    if item["data"] is not None:
        records.append(item["data"])

# DataFrame erstellen
df = pd.DataFrame(records)
print(df)
print(f"\nAnzahl Datensätze: {len(df)}")

# Deutsche Monatsnamen ersetzen
monate = {
    "Januar": "January", "Februar": "February", "März": "March",
    "April": "April", "Mai": "May", "Juni": "June",
    "Juli": "July", "August": "August", "September": "September",
    "Oktober": "October", "November": "November", "Dezember": "December"
}
for de, en in monate.items():
    df["datum"] = df["datum"].str.replace(de, en)

# Datum in einheitliches Format umwandeln
df["datum"] = pd.to_datetime(df["datum"], dayfirst=True, format="mixed")
print(df["datum"])

import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("output/rechnungen.db")

# Daten in die Datenbank laden
df.to_sql("rechnungen", conn, if_exists="replace", index=False)

print("Daten in SQLite gespeichert!")
conn.close()

# SQL-Abfragen ausführen
conn = sqlite3.connect("output/rechnungen.db")

# Ausgaben pro Lieferant
print("\nAusgaben pro Lieferant:")
result = pd.read_sql("SELECT lieferant, SUM(brutto) as gesamt FROM rechnungen GROUP BY lieferant ORDER BY gesamt DESC", conn)
print(result)

# Ausgaben pro Monat
print("\nAusgaben pro Monat:")
result2 = pd.read_sql("SELECT strftime('%Y-%m', datum) as monat, SUM(brutto) as gesamt FROM rechnungen GROUP BY monat ORDER BY monat", conn)
print(result2)

conn.close()