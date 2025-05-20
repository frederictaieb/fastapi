# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser le frontend Next.js à accéder à l'API
origins = [
    "http://localhost:3000",  # Adresse du frontend Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/items")
def get_items():
    return [
        {"id": 1, "name": "Stylo"},
        {"id": 2, "name": "Cahier"},
        {"id": 3, "name": "Livre"},
    ]
