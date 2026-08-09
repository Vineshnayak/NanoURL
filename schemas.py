from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class URLBase(BaseModel):
    original_url: HttpUrl

class URLCreate(URLBase):
    pass

class URLInfo(URLBase):
    short_code: str
    created_at: datetime
    clicks: int
    expires_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class URLStats(BaseModel):
    short_code: str
    clicks: int
    created_at: datetime
