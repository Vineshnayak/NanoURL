from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from core.base62 import encode

router = APIRouter(prefix="/api/v1", tags=["urls"])

@router.post("/shorten", response_model=schemas.URLInfo)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    # Create the db record to get the auto-incremented ID
    db_url = models.URLMapping(original_url=str(url.original_url))
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    # Generate short_code using Base62 encoding of the ID
    db_url.short_code = encode(db_url.id)
    db.commit()
    db.refresh(db_url)
    
    return db_url
