from typing import Optional
from pydantic import BaseModel


class NoteBase(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    category: str = "General"


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int


class NotesResponse(BaseModel):
    message: str
    notes: list[Note]