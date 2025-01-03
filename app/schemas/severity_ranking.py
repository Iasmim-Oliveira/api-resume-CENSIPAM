from pydantic import BaseModel

class SeverityRankingSchema(BaseModel):
    id_evento: int
    severidade: float
    duracao_evento: int
    area_evento: int
    uf: str
    cidade: str

    class Config:
        orm_mode = True