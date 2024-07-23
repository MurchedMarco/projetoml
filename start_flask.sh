#!/bin/bash

# Ativa o ambiente virtual, se necessário
# source /caminho/para/seu/venv/bin/activate

# Define as variáveis de ambiente para o Flask
export FLASK_APP=app.py
export FLASK_ENV=development

# Abre o navegador padrão no endereço do Flask
xdg-open http://127.0.0.1:5000/ &

# Inicia o servidor Flask
flask run
