# Medical Equipment Manager

Backend system for managing medical equipment and incidents in a clinical environment, built with Python and SQLite.

## About

This project was built as a portfolio piece during my transition from **Biomedical Engineering** to **Software Development**. Having worked hands-on with medical equipment from companies like Siemens Healthineers, Roche, Bruker, Sysmex, Inpeco and Edwards Lifesciences, I designed this system based on real-world needs in clinical environments.

## Features

- Full CRUD for medical equipment (create, read, update, delete)
- Full CRUD for incidents linked to equipment
- Automatic incident timestamping
- Input validation and error handling
- Relational database with foreign key constraints
- SQL JOIN queries to display enriched incident data

## Tech Stack

- **Python 3.12** — OOP, modular architecture
- **SQLite3** — relational database
- **datetime** — automatic incident timestamps
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server

## Project Structure
medical-equipment-manager/
│
├── database.py          # Database connection
├── models.py            # Table creation and initial data
├── main.py              # Entry point and CLI menu
│
└── crud/
├── init.py
├── equipos.py       # Equipment CRUD class
└── incidencias.py   # Incidents CRUD class

## REQUIREMENTS

- Python 3.8 or higher

## How to Run

Clone the repository and run:

```bash
git clone https://github.com/edoardopg/medical-equipment-manager.git
cd medical-equipment-manager
python main.py
```

No external dependencies required. The database file `data.db` is created automatically on first run.

## Roadmap

- [ ] Web interface (HTML/CSS/JS)
- [ ] User authentication
- [ ] Docker support

## Author

Edoardo — Biomedical Engineer transitioning to Software Development.