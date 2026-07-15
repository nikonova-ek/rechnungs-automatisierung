# Automatisierte Rechnungsverarbeitung

## Problem
Manuelle Erfassung von Rechnungsdaten kostet ca. 15 Min. pro Rechnung.

## Lösung
PDF-Rechnungen werden automatisch verarbeitet:
1. Text-Extraktion per pdfplumber
2. Strukturierte Datenextraktion per LLM (Ollama/llama3.2)
3. Datenbereinigung und Speicherung in SQLite-Datenbank
4. Auswertung nach Lieferant und Monat

## Tech-Stack
- Python (pdfplumber, pandas, sqlite3)
- LLM-Extraktion (Ollama / llama3.2)
- SQL (SQLite)
- Excel-Automatisierung (openpyxl) — in Entwicklung
- Power BI Dashboard — in Entwicklung
- AI Agent (n8n) — in Entwicklung

## Projektstruktur