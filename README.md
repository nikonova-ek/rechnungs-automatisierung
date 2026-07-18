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

## Tech-Stack
- Python (pdfplumber, pandas, sqlite3)
- LLM-Extraktion (Ollama / llama3.2)
- SQL (SQLite)
- Excel-Automatisierung (openpyxl) — zwei Blätter, bedingte Formatierung
- Power BI Dashboard — in Entwicklung
- AI Agent (n8n) — in Entwicklung

## Projektstruktur

## Excel-Report
Zwei Blätter:
- **Daten** — alle Rechnungen mit Feldern: Rechnungsnr., Datum, Lieferant, Netto, MwSt, Brutto
- **Auswertung** — Ausgaben pro Lieferant und pro Monat. Teuerster Lieferant wird automatisch rot markiert.
