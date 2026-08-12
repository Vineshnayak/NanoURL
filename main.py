from fastapi import FastAPI
import models
from database import engine
from api.routes import router as api_router

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NanoURL API", description="A simple URL shortener")

app.include_router(api_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
