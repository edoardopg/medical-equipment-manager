# Medical Equipment Manager

Full-stack system for managing medical equipment and incidents in a clinical environment, built with Python, FastAPI and SQLite.

## About

This project was built as a portfolio piece during my transition from **Biomedical Engineering** to **Software Development**. Having worked hands-on with medical equipment from companies like Siemens Healthineers, Roche, Bruker, Sysmex, Inpeco and Edwards Lifesciences, I designed this system based on real-world needs in clinical environments.

## Features

- Full CRUD for medical equipment and incidents via REST API
- JWT authentication with login and session protection
- Automatic incident timestamping
- Input validation and error handling
- Relational database with foreign key constraints
- SQL JOIN queries to display enriched incident data
- Web interface with HTML, CSS and JavaScript

## Tech Stack

- **Python 3.12** — OOP, modular architecture
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server
- **SQLite3** — relational database
- **JWT (python-jose)** — authentication
- **bcrypt** — password hashing
- **HTML/CSS/JavaScript** — frontend

## Project Structure
medical-equipment-manager/
│
├── database.py          # Database connection
├── models.py            # Table creation and initial data
├── main.py              # Entry point
├── api.py               # REST API endpoints
├── login.html           # Login page
├── index.html           # Main dashboard
│
└── crud/
├── init.py
├── equipos.py       # Equipment CRUD class
└── incidencias.py   # Incidents CRUD class
## Requirements

- Python 3.8 or higher
- Install dependencies:

```bash
pip install fastapi uvicorn python-jose bcrypt
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/edoardopg/medical-equipment-manager.git
cd medical-equipment-manager
```

Initialize the database:

```bash
python main.py
```

Start the API server:

```bash
uvicorn api:app --reload
```

Open `login.html` with Live Server and log in with:
- **Username:** admin
- **Password:** admin123

## Roadmap

- [x] REST API with FastAPI
- [x] Web interface (HTML/CSS/JS)
- [x] JWT authentication
- [ ] Deploy to Railway/Render
- [ ] Docker support

## Author

Edoardo — Biomedical Engineer transitioning to Software Development.  
[GitHub](https://github.com/edoardopg)