# 🔌 My-First-FastAPI 🛰️

**Este projeto é um estudo prático para iniciantes em APIs, com o objetivo de mostrar aos recrutadores minha noção básica sobre desenvolvimento de APIs com FastAPI.**

---

## 🛠️ Requisitos

Antes de tudo, instale:

- **Python 3**
- **pip**
- **FastAPI**
- **httpx**
- **Uvicorn** (para rodar localmente)

### Instalação rápida (Linux/WSL2)
```bash
# Instale Python 3 e pip
sudo apt install -y python3 python3-pip

# Instale os pacotes necessários
pip3 install fastapi httpx "uvicorn[standard]"

# Verificação do httpx (opcional)
pip show httpx
# Se não estiver instalado:
pip install httpx

# Ambiente virtual (opcional)
python3 -m venv ambiente
source ambiente/bin/activate
# 💡 Neste projeto, estou rodando diretamente dentro do WSL2, sem ambiente virtual.

# 📁 Rodando o Projeto
1º Baixe os arquivos: matrix.py e historico_api.py
2º No terminal, execute os seguintes comandos em diretórios separados:

# Para subir a API principal (porta 8000)
uvicorn matrix:app --reload
# Para subir o serviço de histórico (porta 8001)
python historico_api.py

#📬 Fazendo Requisições / via curl mais didatico para quem esta começando.
curl -X POST -H "Content-Type: application/json" \
-d '{"user_id": "victor", "item_id": 3}' \
http://127.0.0.1:8001/escolha/
# Altere o valor de item_id de 1 a 3 para testar diferentes escolhas na MATRIX e salvar no histórico.

# 🔍 Consultando Histórico
Todos os registros: http://127.0.0.1:8001/historico/
Registros de um usuário específico: http://127.0.0.1:8001/historico/victor/

# 💡 Muito obrigado pela sua visita, bons estudos.
Projeto totalmente executado localmente no WSL2
Ideal para iniciantes testarem comunicação entre serviços usando POST e GET
Estrutura clara para aprendizado de APIs REST com Python