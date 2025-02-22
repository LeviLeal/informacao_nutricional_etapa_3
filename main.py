from fastapi import FastAPI
from rotas import home, usuarios, refeicoes, alimentos

# FastAPI app instance
app = FastAPI()

# Rotas para Endpoints
app.include_router(home.router)
app.include_router(usuarios.router)
app.include_router(refeicoes.router)
app.include_router(alimentos.router)