from pydantic import BaseModel

class AcumulatedBiomeSchema(BaseModel):
    data: str
    numero_eventos: int
    
    class Config:
        orm_mode = True