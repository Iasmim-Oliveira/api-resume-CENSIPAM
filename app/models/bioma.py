from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Bioma(Base):
    __tablename__ = "queimadas.tb_bioma_subdividida"

    id = Column(Integer, primary_key=True)
    cd_bioma = Column(Integer, nullable=False)