from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import words

app = FastAPI(title="Korean Word Associations API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(words.router, prefix="/api/words", tags=["words"])

@app.get("/")
def root():
    return {"message": "Welcome to the Korean Word Associations API!"}