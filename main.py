from fastapi import FastAPI
import models
from database import engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NanoURL API", description="A simple URL shortener")

@app.get("/health")
def health_check():
    return {"status": "ok"}
