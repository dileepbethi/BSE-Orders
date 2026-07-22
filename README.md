# 📈 OrderIQ – BSE Procurement Intelligence Platform

OrderIQ is an automated procurement intelligence platform that collects corporate announcements from BSE, downloads the associated PDF documents, extracts structured order information, validates the extracted data through a human review workflow, and prepares trusted datasets for analytics and future AI-powered insights.

---

## 🚀 Project Overview

This project automates the complete workflow of converting unstructured BSE corporate announcement PDFs into structured, validated business data.

Current workflow:

```text
BSE Website
      │
      ▼
Scraper
      │
      ▼
PDF Downloader
      │
      ▼
PDF Parser
      │
      ▼
Field Cleaner
      │
      ▼
Structured JSON
      │
      ▼
SQLite Database
      │
      ▼
Accuracy Framework
      │
      ▼
Review Tool
      │
      ▼
Gold Dataset
```

---

## ✨ Current Features

- ✅ Automated BSE announcement scraping
- ✅ Automatic PDF downloading
- ✅ PDF text extraction
- ✅ Structured field extraction
- ✅ Field cleaning & normalization
- ✅ SQLite database storage
- ✅ Accuracy validation framework
- ✅ Human review interface
- ✅ Gold dataset generation

---

## 📂 Project Structure

```text
scripts/          → Scraper, parser and processing scripts
review_tool/      → Human review application
database/         → SQLite database
data/             → Processed data and datasets
reports/          → Accuracy reports
logs/             → Execution logs
```

---

## 🛠 Tech Stack

- Python
- Playwright
- SQLite
- Flask
- JSON
- Git & GitHub

---

## 📌 Current Status

| Module | Status |
|---------|--------|
| Scraper | ✅ Complete |
| Downloader | ✅ Complete |
| Parser | ✅ Complete |
| Accuracy Framework | ✅ Complete |
| Review Tool | ✅ Complete |
| Gold Dataset | ✅ Complete |
| REST API | 🚧 Planned |
| Dashboard | 🚧 Planned |
| AI Insights | 🚧 Planned |

---

## 🎯 Vision

Build an intelligence platform that transforms public procurement announcements into structured, searchable, and actionable business intelligence for investors, analysts, and enterprises.

---

## 📅 Roadmap

### Phase 1
- BSE Scraper ✅
- PDF Downloader ✅
- Parser ✅
- Review Tool ✅

### Phase 2
- REST API
- Dashboard
- Search & Filters

### Phase 3
- AI Insights
- Analytics
- Procurement Intelligence Platform