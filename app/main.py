from fastapi import FastAPI
from app.routes import router as notes_router

app = FastAPI()
app = FastAPI(title="A Simple Note Taking API")

app.include_router(notes_router, prefix="/notes", tags=["Notes"])

@app.get("/")
def root():
    return { "message": "Welcome to the Note Taking API",
             "route": "/notes",
             "swaggerDoc": '/docs',
             "ReDoc": '/redoc'
            }
