from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db
from app.schemas import AcumulatedBiomeSchema

router = APIRouter()

@router.get("/acumulado-bioma", response_model=list[AcumulatedBiomeSchema])
def getAcumulatedBiome (db: Session = Depends(get_db)):
    query = """
        WITH RECURSIVE DateRange AS (
            SELECT '2024-01-01'::date AS dt
            UNION ALL
            SELECT (dt + INTERVAL '1 day')::date
            FROM DateRange
            WHERE (dt + INTERVAL '1 day') <= '2025-01-01'::date
        ),
        EventosFogo AS (
            SELECT 
                DATE(ev1.dt_minima) AS dt_minima,
                COUNT(ev1.dt_minima) AS num_eventos
            FROM 
                queimadas.tb_evento AS ev1
            JOIN 
                bases_auxiliares.ibge_bc250_lim_unidade_federacao_a AS ep 
                ON ST_Intersects(ev1.geom, ep.geom) -- Interseção com a máscara de escopo espacial
            JOIN 
                queimadas.tb_escopo_queimadas AS escopo
                ON ST_Intersects(ev1.geom, escopo.geom)
            JOIN 
                queimadas.tb_bioma_subdividida AS bioma
                ON ST_Intersects(ev1.geom, bioma.geom)
            WHERE 
                ev1.id_status_evento IN (1, 2, 3) -- Condição de eventos ativos, em observação
                AND ev1.area_km2 > 1 -- Condição de área maior que 1km2
                AND bioma.cd_bioma = 6 -- Filtro para o bioma Pantanal
                AND ev1.dt_minima >= '2024-01-01'
                AND ev1.dt_minima <= '2025-01-01' -- Define período a ser investigado
            GROUP BY 
                DATE(ev1.dt_minima)
        )
        SELECT 
            dr.dt AS "Data",
            COALESCE(ef.num_eventos, 0) AS "Num. de Eventos"
        FROM 
            DateRange dr
        LEFT JOIN 
            EventosFogo ef
        ON 
            dr.dt = ef.dt_minima
        ORDER BY 
            dr.dt ASC;
    
    """
    
    result = db.execute(text(query)).fetchall()
    
    events = [
        AcumulatedBiomeSchema(
            data = row[0].strftime('%Y-%m-%d'),
            numero_eventos = row[1]
        )
        for row in result
    ]
    
    return events