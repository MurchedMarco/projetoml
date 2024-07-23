import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def salva_objeto(caminho_arquivo, obj):
    try:
        caminho_dir = os.path.dirname(caminho_arquivo)

        os.makedirs(caminho_dir, exist_ok=True)

        with open(caminho_arquivo, "wb") as arquivo_obj:
            pickle.dump(obj, arquivo_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def avalia_modelos(X_treino, y_treino,X_teste,y_teste,modelos,param):
    try:
        relatorio = {}

        for i in range(len(list(modelos))):
            modelo = list(modelos.values())[i]
            para=param[list(modelos.keys())[i]]

            gs = GridSearchCV(modelo,para,cv=3)
            gs.fit(X_treino,y_treino)

            modelo.set_params(**gs.best_params_)
            modelo.fit(X_treino,y_treino)

            #modelo.fit(X_treino, y_treino)  # Treina modelo

            y_treino_pred = modelo.predict(X_treino)

            y_teste_pred = modelo.predict(X_teste)

            modelo = r2_score(y_treino, y_treino_pred)

            test_modelo_pontuacao = r2_score(y_teste, y_teste_pred)

            relatorio[list(modelos.keys())[i]] = test_modelo_pontuacao

        return relatorio

    except Exception as e:
        raise CustomException(e, sys)
    
def carrega_objeto(caminho_arquivo):
    try:
        with open(caminho_arquivo, "rb") as arquivo_obj:
            return pickle.load(arquivo_obj)

    except Exception as e:
        raise CustomException(e, sys)