from fastapi import APIRouter, HTTPException
from app.schemas import Note, NoteCreate, NotesResponse

router = APIRouter()

notes_db = []

@router.get("", response_model=NotesResponse)
async def get_all_notes():
    """Fetch all notes currently in memory."""
    return { "message": f"Total notes: {len(notes_db)}", "notes": notes_db }

@router.post("", response_model=Note, status_code=201)
async def create_note(note: NoteCreate):
    """Save a new note to the list."""
    note_id = notes_db[-1].id + 1 if notes_db else 1
    payload = note.model_dump(exclude={"id"})
    new_note = Note(id=note_id, **payload)

    notes_db.append(new_note)
    return new_note

@router.get("/{note_id}", response_model=Note)
async def get_single_note(note_id: int):
    """Find a specific note by its ID."""
    for note in notes_db:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

@router.put("/{note_id}")
async def update_note(note_id: int, updated_note: NoteCreate):
    """Update a note in the list."""
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            payload = updated_note.model_dump(exclude={"id"})
            notes_db[index] = Note(id=note_id, **payload)
            return notes_db[index]
    raise HTTPException(status_code=404, detail="Note not found")

@router.delete("/{note_id}", status_code=204, responses={204: {"description": "No Content"}})
async def delete_note(note_id: int):
    """Remove a note from the list."""
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db.pop(index)
            return None
    raise HTTPException(status_code=404, detail="Note not found")