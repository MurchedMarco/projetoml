import logging
import os
from datetime import datetime

ARQUIVO_LOG=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
caminho_logs=os.path.join(os.getcwd(),"logs",ARQUIVO_LOG)
os.makedirs(caminho_logs,exist_ok=True)

ARQUIVO_LOG_PATH=os.path.join(caminho_logs,ARQUIVO_LOG)

logging.basicConfig(
    filename=ARQUIVO_LOG_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)