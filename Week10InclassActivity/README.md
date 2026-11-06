# Library App (Weeks 10–11)

This project uses one SQLite `Book` model with two interfaces:

- **Week 10 web app:** Flask routes in `app.py` and pages in `templates/` let you list, view, add, and edit books.
- **Week 11 phone app:** Flet controls in `main.py` let you list, search, add, and delete books. Input is checked before saving.

Both interfaces use `models.py` and the same local `library.db` file.

## Set up on macOS

Open a terminal in this `Week10InclassActivity` folder, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install flask 'flet[all]'
python setup_db.py
```

Run `setup_db.py` only when creating the database or intentionally resetting it. **Running it again deletes all current books** and restores the three sample books.

## Run the web app

```bash
python -m flask --app app run --debug
```

Open <http://127.0.0.1:5000/books> in your browser. Stop the server with `Ctrl+C`.

## Run the Flet app

For a desktop window:

```bash
flet run main.py
```

For a phone, install the Flet app, connect the phone and computer to the same Wi-Fi, and run one of these commands:

```bash
flet run --ios main.py      # iPhone
flet run --android main.py  # Android
```

Scan the QR code shown in the terminal. Keep the terminal running while using the app. The Python code and database stay on the computer.

## Files

| File | Purpose |
| --- | --- |
| `setup_db.py` | Creates the database and three sample books |
| `models.py` | Defines `Book` and its SQLite operations |
| `app.py` | Flask web routes |
| `templates/` | Web page templates |
| `main.py` | Flet interface and event handlers |

`library.db`, `.venv`, and Python cache files are local runtime files and do not need to be uploaded to GitHub.
