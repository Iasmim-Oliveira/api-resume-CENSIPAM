from fastapi import FastAPI
from app.api.endpoints.biomas import router as biomas_router

app = FastAPI()

# Adicionando o router
app.include_router(biomas_router)
