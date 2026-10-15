# 🏢 Dallas Apartment Parser

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)]()

> A robust ETL (Extract, Transform, Load) pipeline and web dashboard for scraping, cleaning, and visualizing apartment rental listings from the Nestpick API (Dallas, TX). Built with a strong focus on clean architecture, strict type hinting, and safe resource management.

## 📋 About the Project

This project automatically parses real estate listings, transforms raw JSON data into a structured format, and saves it simultaneously to two destinations:
1. **JSON file** (for quick inspection and backup).
2. **SQLite database** (for structured storage and web visualization).

Additionally, it includes a lightweight **Flask web interface** to browse the collected data directly in the browser.

##  Key Features

- ✅ **Robust Scraping:** Uses `requests` with realistic browser headers and strict `timeout` settings to bypass basic anti-bot protections.
- ✅ **Custom Context Managers:** Native implementation of `__enter__` and `__exit__` in `ToJson` and `ToDataBase` classes, guaranteeing safe closure of files and database connections.
- ✅ **Duplicate Protection:** Utilizes `UNIQUE` constraints and `INSERT OR IGNORE` in SQLite to ensure idempotent data loading.
- ✅ **Strict Type Hinting:** Fully annotated code (`typing.Any`, `types.TracebackType`) for better IDE support and maintainability.
- ✅ **Clean Architecture:** Clear Separation of Concerns (SRP) across independent classes: `Parser`, `ToJson`, and `ToDataBase`.
- ✅ **Web Dashboard:** A simple Flask app to visualize apartments with prices, photos, and descriptions.

## 🛠 Tech Stack

- **Language:** Python 3.12+
- **Data Extraction:** `requests`
- **Storage:** `sqlite3` (built-in), `json` (built-in)
- **Web Framework:** `Flask`
- **Typing:** `typing`, `types`

## 📁 Project Structure

```text
apartment-parser/
├── parser.py              # Main script containing parsing and export logic
├── app.py                 # Flask web application
├── templates/
│   └── index.html         # HTML template for the web dashboard
├── apartments.db          # SQLite database (gitignored)
── apartment_test.json    # JSON export of the data (gitignored)
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/Mishel067/apartment-parser.git
cd apartment-parser
```

### 2. Set up a virtual environment (Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the ETL Pipeline
To fetch data and populate the database:
```bash
python parser.py
```

### 5. Launch the Web Dashboard
To view the apartments in your browser:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

## 🗄️ Database Schema

The `apartment` table is structured as follows:
```sql
CREATE TABLE IF NOT EXISTS apartment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number_of_bedrooms INTEGER,
    category TEXT,
    apartment_size INTEGER,
    price INTEGER,
    name TEXT,
    description TEXT,
    url TEXT UNIQUE,       -- Ensures no duplicate listings are inserted
    photos TEXT
)
```

## 🗺️ Roadmap

- [ ] **v0.2:** Integrate the `logging` module to replace `print()` statements.
- [ ] **v0.3:** Externalize configuration (API URLs, DB paths) using a `.env` file.
- [ ] **v0.4:** Add support for multiple cities (e.g., New York, Austin).
- [ ] **v0.5:** Containerize the application using Docker.

##  License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
*Made with ❤️ and Python by [Mishel067](https://github.com/Mishel067)*
