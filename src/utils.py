import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def salva_objeto(caminho_arquivo, obj):
    try:
        dir_path = os.path.dirname(caminho_arquivo)
        os.makedirs(dir_path, exist_ok = True)
        with open(caminho_arquivo, 'wb') as arq_obj:
            dill.dump(obj, arq_obj)
    except Exception as e:
        raise CustomException(e, sys)
    