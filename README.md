# My-First-FastAPI
**O objetivo é servir como um projeto de estudo para iniciantes em APIs e mostrar para recrutadores minha noção básica sobre API.**

|  Para testar o projeto instale primeiro: Python, Pip, FastAPI e Httpx. (Instale o Uvicorn também  para testar localmente)

*Instale python 3 e pip = ``sudo apt install -y python3 python3-pip``
*Instale os pacotes Python necessários = ``pip3 install fastapi httpx "uvicorn[standard]"``

Se quiser verificar se a instalação do httpx deu certo, rode: `pip show httpx` se não rode `pip install httpx`

Caso queira pode rodar em ambiente virtual usando ``python3 -m venv ambiente``, que não é meu caso. (Estou rodando direto dentro do WSL2)

Após a instalação necessária, baixe os arquivos [ main.py ]

**| 1ºAbra o terminal no diretorio do matrix.py e rode com: `uvicorn matrix:app --reload` (porta 8000 padrão)**
**| 2ºRode o historico_py.py com: `python historico_api.py` (porta 8001 configurada)**

Após os dois estarem rodando localmente, você pode fazer o post pela interface do FastAPI em "/docs" ou usar o curl que é mais didatico para quem esta iniciando.
**Exemplo:** curl -X POST -H "Content-Type: application/json" -d '{"user_id": "victor", "item_id": 3}' http://127.0.0.1:8001/escolha/

Em `"item_id": x` alterne `x` entre 1 á 3 para fazer o post de escolhas diferentes na MATRIX, e salvar no histórico.

Para consultar `GET`, vai esta disponível em: http://127.0.0.1:8001/historico/ ou se quiser só consultar escolhas de um user especifico http://127.0.0.1:8001/historico/victor/