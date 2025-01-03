from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db
from app.schemas import SeverityRankingSchema

router = APIRouter()

@router.get("/ranking-severidade", response_model=list[SeverityRankingSchema])
def getSeverityRanking (db: Session = Depends(get_db)):
    query = """
    WITH RankedEventos AS (
  SELECT
    id_evento,
    peso_global_passagem,
    tempo_acumulado_horas,
    ROW_NUMBER() OVER (PARTITION BY id_evento ORDER BY peso_global_passagem DESC) AS rn_peso,
    ROW_NUMBER() OVER (PARTITION BY id_evento ORDER BY tempo_acumulado_horas DESC) AS rn_tempo,
	area_total_evento_ha,
	i.sigla,
        m.nome,
        m.sg_uf
  FROM queimadas.mv_indicadores_queimadas q
  JOIN bases_auxiliares.ibge_bc250_lim_unidade_federacao_a i ON ST_Intersects(i.geom, q.geom_acumulada)
  JOIN bases_auxiliares.ibge_bc250_lim_municipio_a m ON ST_Intersects(m.geom, q.geom_acumulada)
  WHERE 
	 q.dt_max_evento >= now () - interval '1 day'
)
SELECT
  r1.id_evento as "ID do Evento",
  round(cast(r1.peso_global_passagem as numeric), 2) AS "Severidade",
  cast(r2.tempo_acumulado_horas as integer) / 24 AS "Duração do Evento",
  cast(r1.area_total_evento_ha as integer) "Área do Evento (ha)",
  r1.nome AS "Município",
  r1.sg_uf AS "UF"
FROM RankedEventos r1
JOIN RankedEventos r2 ON r1.id_evento = r2.id_evento
WHERE r1.rn_peso = 1 AND r2.rn_tempo = 1
ORDER BY r1.peso_global_passagem DESC
LIMIT 10;
        """
    
    result = db.execute(text(query)).fetchall()
    
    events = [
        SeverityRankingSchema(
            id_evento=row[0],
            severidade=row[1],
            duracao_evento=row[2],
            area_evento=row[3],
            uf=row[4],
            cidade=row[5]
        )
        for row in result
        ]
    
    return events
