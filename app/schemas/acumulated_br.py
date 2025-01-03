from pydantic import BaseModel

class AcumulatedBrazilSchema(BaseModel):
    numero_eventos: int
    data: str
    
    class Config:
        orm_mode = True
    