from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db

router = APIRouter(prefix="/api/v1", tags=["urls"])

@router.post("/shorten", response_model=schemas.URLInfo)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    # Create the db record to get the auto-incremented ID
    db_url = models.URLMapping(original_url=str(url.original_url))
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    # Temporary: set short_code to stringified ID just to pass schema validation
    # This will be replaced with Base62 encoding in the next phase
    db_url.short_code = str(db_url.id)
    
    return db_url
