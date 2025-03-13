from pydantic import BaseModel

class QRRequest(BaseModel):
    link: str
