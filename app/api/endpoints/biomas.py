from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

router = APIRouter()

# Modelo para a resposta da API
class BiomaEventoResponse(BaseModel):
    bioma: str
    quantidade_eventos: int

@router.get("/biomas", response_model=List[BiomaEventoResponse])
def getEventsByBiome(
        startDate: date,
        endDate: date,
        bioma_id: Optional[int] = None, 
        db: Session = Depends(get_db)
): 
    try:
        query = """
        SELECT
            CASE
                WHEN bio.cd_bioma = 1 THEN 'AMAZÔNIA'
                WHEN bio.cd_bioma = 2 THEN 'CAATINGA'
                WHEN bio.cd_bioma = 3 THEN 'CERRADO'
                WHEN bio.cd_bioma = 4 THEN 'MATA ATLÂNTICA'
                WHEN bio.cd_bioma = 5 THEN 'PAMPA'
                WHEN bio.cd_bioma = 6 THEN 'PANTANAL'
                ELSE bio.cd_bioma::TEXT
            END AS "Bioma",
            COUNT(DISTINCT(q)) AS "quantidade_eventos"
        FROM queimadas.tb_bioma_subdividida bio
        LEFT JOIN queimadas.tb_evento q
            ON ST_Within(q.geom, bio.geom)
        WHERE q.dt_maxima BETWEEN :data_inicio AND :data_fim
        """

        # Adiciona o filtro pelo bioma se o bioma_id for passado
        if bioma_id:
            query += " AND bio.cd_bioma = :bioma_id"

        query += """
        GROUP BY bio.cd_bioma
        ORDER BY "Bioma";
        """
        
        # Executa a query com os parâmetros
        result = db.execute(text(query), {"data_inicio": startDate, "data_fim": endDate, "bioma_id": bioma_id if bioma_id else None}).fetchall()

        # Retorna a resposta no formato esperado
        return [
            {"bioma": row[0], "quantidade_eventos": row[1]}
            for row in result
        ]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
