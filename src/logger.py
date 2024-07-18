import logging
import os
from datetime import datetime

# Configuração do logging
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs')

if not os.path.exists(logs_path):
    os.makedirs(logs_path)

LOG_FILE_PATH = os.path.abspath(os.path.join(logs_path, LOG_FILE))

try:
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
    )
except Exception as e:
    print(f"Erro ao configurar o logging: {e}")

# Chama a função que você deseja registrar no log
try:
    a = 1/0
except ZeroDivisionError as e:
    logging.error(f'Não pode dividir por ZERO.\n Arquivo de log: {LOG_FILE}')
    print(f"Erro: {e}")
    print(f"Arquivo de log: {LOG_FILE}")
