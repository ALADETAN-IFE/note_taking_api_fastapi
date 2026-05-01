# Note Taking API (FastAPI)

Small FastAPI app that stores notes in memory while the server runs. Intended for learning and quick demos.

## Prerequisites

- Python 3.10+ (any modern Python 3.x should work)
- See `requirements.txt` for runtime dependencies (`fastapi`, `uvicorn`, `pydantic`).

## Install

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows (Git Bash / WSL)
\.venv\Scripts\activate       # Windows CMD/PowerShell
pip install --upgrade pip
pip install -r requirements.txt
```

## Run (development)

Start the app with uvicorn (auto-reload):

```bash
uvicorn app.main:app --reload
```

Open the interactive docs at:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

All endpoints are under the `/notes` prefix.

- GET `/notes` — list all notes. Returns `200` and a JSON array of notes.
- POST `/notes` — create a note. Returns `201` and the created note.
- GET `/notes/{note_id}` — fetch a note by its ID. Returns `200` or `404`.
- PUT `/notes/{note_id}` — update a note. Returns `200` or `404`.
- DELETE `/notes/{note_id}` — delete a note. Returns `204 No Content` on success or `404`.

Note JSON shape:

```json
{
  "id": 1,
  "title": "Groceries",
  "content": "Milk, bread, eggs",
  "category": "General"
}
```

`category` defaults to `General` when omitted.

## Examples

Create a note with `curl`:

```bash
curl -s -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"Groceries","content":"Milk, bread, eggs"}'
```

Delete a note (expect `204`):

```bash
curl -i -X DELETE http://127.0.0.1:8000/notes/1
```

## Notes

- The app uses an in-memory list; all data is lost on restart.
