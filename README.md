# Automatisierte Rechnungsverarbeitung

## Problem
Manuelle Erfassung von Rechnungsdaten kostet ca. 15 Min. pro Rechnung.

## Lösung
PDF-Rechnungen werden automatisch verarbeitet: Text-Extraktion per pdfplumber,
strukturierte Datenextraktion per LLM (Ollama/llama3.2), Speicherung in SQLite-Datenbank,
Auswertung in Excel und Power BI.

## Tech-Stack
- Python (pdfplumber, pandas, openpyxl)
- LLM-Extraktion (Ollama/llama3.2)
- SQL (SQLite)
- Excel-Automatisierung (openpyxl)
- Power BI

## Status
In Entwicklung — Schritt 1 (PDF-Extraktion) abgeschlossen.