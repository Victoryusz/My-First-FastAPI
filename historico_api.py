from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from datetime import datetime
from typing import List
import uvicorn

app = FastAPI()

# Endereço da API original
MATRIX_API_URL = "http://127.0.0.1:8000/escolhas/"

# Modelo para entrada de escolha
class EscolhaInput(BaseModel):
    user_id: str
    item_id: int

# Modelo para histórico de escolhas
class EscolhaHistorico(BaseModel):
    user_id: str
    item_id: int
    escolha: str
    mensagem: str
    frase: str
    timestamp: datetime

# Armazenamento em memória para o histórico
historico: List[EscolhaHistorico] = []

@app.post("/escolha/", response_model=EscolhaHistorico)
async def registrar_escolha(escolha: EscolhaInput):
    # Faz requisição à API original
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{MATRIX_API_URL}{escolha.item_id}")
            response.raise_for_status()
            data = response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=400, detail="Erro ao consultar a Matrix API. Verifique o item_id.")
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Não foi possível conectar à Matrix API.")

    # Verifica se a escolha é válida
    if "message" in data and "Escolha não encontrada" in data["message"]:
        raise HTTPException(status_code=404, detail=data["message"])

    # Cria registro para o histórico
    registro = EscolhaHistorico(
        user_id=escolha.user_id,
        item_id=data["item_id"],
        escolha=data["escolha"],
        mensagem=data["message"],
        frase=data["frase"],
        timestamp=datetime.now()
    )
    
    # Adiciona ao histórico
    historico.append(registro)
    return registro

@app.get("/historico/", response_model=List[EscolhaHistorico])
async def consultar_historico():
    return historico

@app.get("/historico/{user_id}", response_model=List[EscolhaHistorico])
async def consultar_historico_usuario(user_id: str):
    usuario_historico = [item for item in historico if item.user_id == user_id]
    if not usuario_historico:
        raise HTTPException(status_code=404, detail="Nenhuma escolha encontrada para este usuário.")
    return usuario_historico

@app.delete("/historico/")
async def limpar_historico():
    historico.clear()
    return {"message": "Histórico limpo com sucesso."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)