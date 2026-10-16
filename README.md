# 🏢 Dallas Apartment Parser

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Live-green.svg)](https://mishel067.pythonanywhere.com/)

> A live web dashboard that aggregates and visualizes apartment rental listings from Dallas, TX. Built as a full ETL pipeline — from API scraping to a Flask-powered frontend with automated background data refresh.

## 🌐 Live Demo

👉 **[Open the website: mishel067.pythonanywhere.com](https://mishel067.pythonanywhere.com/)**

No installation required. The site is deployed and running 24/7 on PythonAnywhere.

## 📋 About the Project

This project solves a real problem: finding affordable apartments in Dallas. It automatically fetches listings from the Nestpick API, cleans and structures the data, stores it in a SQLite database, and presents it through a clean web interface.

Instead of manually browsing dozens of pages, users can see all available apartments in one place, sorted by price, with photos, descriptions, and direct links to the original listings.

## ✨ Key Features

- ✅ **Live Web Dashboard** — Browse 40+ apartments with prices, photos, and descriptions.
- ✅ **Automated ETL Pipeline** — Fetches data from Nestpick API, transforms it, and loads it into SQLite.
- ✅ **Scheduled Data Refresh** — APScheduler automatically updates the database every 24 hours in the background.
- ✅ **Duplicate Protection** — `UNIQUE` constraints and `INSERT OR IGNORE` prevent duplicate entries.
- ✅ **Clean Architecture** — Separation of concerns: `Parser`, `ToJson`, `ToDataBase` classes.
- ✅ **Custom Context Managers** — Safe resource handling with `__enter__` / `__exit__`.
- ✅ **Structured Logging** — Professional logging with traceback support for robust debugging.
- ✅ **Docker Support** — One-command deployment with containerization.
- ✅ **Strict Type Hinting** — Full annotations for maintainability.

## 🛠 Tech Stack

- **Backend:** Python 3.12+, Flask, APScheduler
- **Data Extraction:** `requests`
- **Storage:** `sqlite3`
- **Frontend:** HTML5, CSS3 (vanilla)
- **Deployment:** PythonAnywhere, Docker
- **Version Control:** Git + GitHub

## 📁 Project Structure

```text
apartment-parser/
├── parser_.py             # ETL pipeline (API → JSON → SQLite)
├── app.py                 # Flask web app with background scheduler
├── templates/
│   └── index.html         # Dashboard UI
├── requirements.txt       # Python dependencies
├── Dockerfile             # Containerization ready
├── .dockerignore          # Docker ignore rules
├── .gitignore             # Git ignore rules
└── README.md
```

## ⚙️ Run Locally (Optional)

```bash
git clone https://github.com/Mishel067/apartment-parser.git
cd apartment-parser

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
python parser_.py         # Fetch data manually (optional)
python app.py             # Start the web server at http://127.0.0.1:5000
```

## 🐳 Run with Docker (Recommended)

```bash
docker build -t apartment-parser .
docker run -p 5000:5000 apartment-parser
```
Open your browser at `http://localhost:5000`.

## 🗄️ Database Schema

```sql
CREATE TABLE IF NOT EXISTS apartment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number_of_bedrooms INTEGER,
    category TEXT,
    apartment_size INTEGER,
    price INTEGER,
    name TEXT,
    description TEXT,
    url TEXT UNIQUE,
    photos TEXT
)
```

## 🗺️ Roadmap

- [x] **v0.2** — Structured logging (`logging` module instead of `print`)
- [x] **v0.3** — Docker containerization for one-command deployment
- [x] **v0.4** — Automated daily data refresh (APScheduler)
- [ ] **v0.5** — Detailed apartment page with full description
- [ ] **v0.6** — Interactive map (Leaflet.js + OpenStreetMap) showing apartment locations
- [ ] **v0.7** — Filters by price, bedrooms, and category
- [ ] **v1.0** — Multi-city support (New York, Austin, etc.)

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
*Made with ❤️ and Python by [Mishel067](https://github.com/Mishel067)*

