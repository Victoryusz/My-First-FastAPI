from fastapi import FastAPI
import uvicorn

matrix = {
    1: {
        "status": "Dead",
        "descricao": "Sua jornada termina aqui.",
        "frase": "Desejamos sorte na próxima...",
    },
    2: {
        "status": "Alive",
        "descricao": "Bem vindo de volta ao mundo 'Real'.",
        "frase": "Continue na ignorância confortável e perdido na ilusão e não questione nada.",
    },
    3: {
        "status": "Between life and death",
        "descricao": "Sua jornada começa agora.",
        "frase": "Você despertou e agora consegue ver o código da Matrix.",
    },
}

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Boas vindas a Matrix! Experimente o endpoint /escolhas/{item_id} escolha sabiamente, Boa Sorte!!"
    }


@app.get("/escolhas/{item_id}")
def read_item(item_id: int):
    if item_id in matrix:
        escolhas = matrix[item_id]
        return {
            "item_id": item_id,
            "escolha": escolhas["status"],
            "message": escolhas["descricao"],
            "frase": escolhas["frase"],
        }
    else:
        return {"message": "Escolha não encontrada. Tente uma entre 1 a 3."}
