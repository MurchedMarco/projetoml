import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import salva_objeto,avalia_modelos

@dataclass
class ConfigTreinadorModelo:
    caminho_arquivo_modelo_treinado=os.path.join("artefatos","modelo.pkl")

class TreinadorModelo:
    def __init__(self):
        self.config_treinador_modelo=ConfigTreinadorModelo()


    def inicia_treinador_modelo(self,array_treino,array_teste):
        try:
            logging.info("Divisão dados de entrada em treinamento e teste completa.")
            X_treino,y_treino,X_teste,y_teste=(
                array_treino[:,:-1],
                array_treino[:,-1],
                array_teste[:,:-1],
                array_teste[:,-1]
            )
            modelos = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }

            relatorio_modelo:dict=avalia_modelos(X_treino=X_treino,y_treino=y_treino,X_teste=X_teste,y_teste=y_teste,
                                             models=modelos,param=params)
            
            ## Para obter a melhor pontuação do modelo do dicionário
            melhor_pontuacao_modelo = max(sorted(relatorio_modelo.values()))

            ## Para obter o melhor nome do modelo do dicionário

            melhor_nome_modelo = list(relatorio_modelo.keys())[
                list(relatorio_modelo.values()).index(melhor_pontuacao_modelo)
            ]
            melhor_modelo = modelos[melhor_nome_modelo]

            if melhor_pontuacao_modelo<0.6:
                raise CustomException("Melhor modelo NÃO encontrado")
            logging.info(f"Melhor modelo encontrado no conjunto de dados de treinamento e teste")

            salva_objeto(
                caminho_arquivo=self.config_treinador_modelo.caminho_arquivo_modelo_treinado,
                obj=melhor_modelo
            )

            previsao=melhor_modelo.predict(X_teste)

            r2_quadrado = r2_score(y_teste, previsao)
            return r2_quadrado
            



            
        except Exception as e:
            raise CustomException(e,sys)