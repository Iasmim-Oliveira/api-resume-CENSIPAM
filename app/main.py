from fastapi import FastAPI
from app.api.endpoints.biomas import router as biomas_router
from app.api.endpoints.severity_ranking import router as severity_ranking_router
from app.api.endpoints.acumulated_br import router as acumulated_br_router

app = FastAPI()

# Adicionando o router
app.include_router(biomas_router, tags=["Eventos por Biomas"])
app.include_router(severity_ranking_router, tags=["Ranking Severidade CIMAN"])
app.include_router(acumulated_br_router, tags=["Acumulado Brasil CIMAN"])