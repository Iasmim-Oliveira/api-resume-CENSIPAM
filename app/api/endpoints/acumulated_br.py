from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db
from app.schemas import AcumulatedBrazilSchema

router = APIRouter()

@router.get("/acumulado-br", response_model=list[AcumulatedBrazilSchema])
def getAcumulatedBrazil(db: Session = Depends(get_db)):
    query = """
        select
        date(dt_minima),
        count(distinct sq1.id) as n_eventos
        from (
            select distinct ev1.*
            from queimadas.tb_evento as ev1
            join bases_auxiliares.ibge_bc250_lim_unidade_federacao_a as ep on st_intersects(ev1.geom,ep.geom)
            where ev1.id_status_evento IN (1,2,3)
            and ev1.area_km2>1
        ) as sq1
        inner join queimadas.tb_escopo_queimadas as escopo
        on st_intersects(sq1.geom,escopo.geom)
        where sq1.dt_minima>='2024-01-01' and sq1.dt_minima<='2024-02-01'
        group by date(dt_minima)
        order by 1 asc;
    """

    result = db.execute(text(query)).fetchall()

    events = [
        AcumulatedBrazilSchema(
            data=row[0].strftime('%Y-%m-%d'),  # Converte a data para string
            numero_eventos=row[1]
        )
        for row in result
    ]

    return events