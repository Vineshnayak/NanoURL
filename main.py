from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from api.routes import router as api_router

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NanoURL API", description="A simple URL shortener")

app.include_router(api_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URLMapping).filter(models.URLMapping.short_code == short_code).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=db_url.original_url, status_code=302)
