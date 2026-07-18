# Automatisierte Rechnungsverarbeitung

## Problem
Manuelle Erfassung von Rechnungsdaten kostet ca. 15 Min. pro Rechnung.

## Lösung
PDF-Rechnungen werden automatisch verarbeitet:
1. Text-Extraktion per pdfplumber
2. Strukturierte Datenextraktion per LLM (Ollama/llama3.2)
3. Datenbereinigung und Speicherung in SQLite-Datenbank
4. Auswertung nach Lieferant und Monat
5. Excel-Report wird automatisch generiert
6. AI Agent (n8n) klassifiziert Rechnungen — Standard oder Prüfung erforderlich

## Tech-Stack
- Python (pdfplumber, pandas, sqlite3)
- LLM-Extraktion (Ollama / llama3.2)
- SQL (SQLite)
- Excel-Automatisierung (openpyxl) — zwei Blätter, bedingte Formatierung
- Power BI Dashboard — in Entwicklung
- AI Agent (n8n) — Klassifizierung mit Human-in-the-Loop

## Projektstruktur

## Excel-Report
Zwei Blätter:
- **Daten** — alle Rechnungen mit Feldern: Rechnungsnr., Datum, Lieferant, Netto, MwSt, Brutto
- **Auswertung** — Ausgaben pro Lieferant und pro Monat. Teuerster Lieferant wird automatisch rot markiert.

## AI Agent (n8n)
Workflow klassifiziert Rechnungen automatisch:
- **Standard** — Brutto unter 2.000€, wird automatisch verarbeitet
- **Prüfung erforderlich** — Brutto über 2.000€, geht zur manuellen Prüfung (Human-in-the-Loop)

![n8n Workflow](docs/n8n_workflow.png)

