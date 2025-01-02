from pydantic import BaseModel

class BiomaResponse(BaseModel):
    id: int
    cd_bioma: int

    class Config:
        orm_mode=True