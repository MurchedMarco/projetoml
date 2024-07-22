import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import salva_objeto

@dataclass
class ConfiguracaoTransformacaoDados:
    caminho_arquivo_obj_preprocessamento=os.path.join('artefatos',"preprocessamento.pkl")

class TransformacaoDados:
    def __init__(self):
        self.configuracao_transformacao_dados=ConfiguracaoTransformacaoDados()

    def obtem_obj_dados_transformados(self):
        '''
        Essa função é responsável pela transformação dos dados
        '''
        try:
            colunas_numericas = ["writing_score", "reading_score"]
            colunas_categoricas = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Colunas Categoricas: {colunas_categoricas}")
            logging.info(f"Colunas Numéricas: {colunas_numericas}")

            preprocessamento=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,colunas_numericas),
                ("cat_pipelines",cat_pipeline,colunas_categoricas)

                ]


            )

            return preprocessamento
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def inicia_transformacao_dados(self,caminho_treino,caminho_teste):

        try:
            df_treino=pd.read_csv(caminho_treino)
            df_teste=pd.read_csv(caminho_teste)

            logging.info("Leitura de dados de treino e teste completas.")

            logging.info("Obtendo objeto de pré-processamento")

            preprocessamento_obj=self.obtem_obj_dados_transformados()

            nome_coluna_destino="math_score"
            colunas_numericas = ["writing_score", "reading_score"]

            recurso_entrada_df_treino=df_treino.drop(columns=[nome_coluna_destino],axis=1)
            recurso_destino_df_treino=df_treino[nome_coluna_destino]

            recurso_entrada_df_teste=df_teste.drop(columns=[nome_coluna_destino],axis=1)
            recurso_destino_df_teste=df_teste[nome_coluna_destino]

            logging.info(
                f"Aplicando objeto de pré-processamento no dataframe de treinamento e teste de dataframe."
            )

            recurso_destino_df_treino_array=preprocessamento_obj.fit_transform(recurso_entrada_df_treino)
            recurso_entrada_array_teste=preprocessamento_obj.transform(recurso_entrada_df_teste)

            array_treino = np.c_[
                recurso_destino_df_treino_array, np.array(recurso_destino_df_treino)
            ]
            array_teste = np.c_[recurso_entrada_array_teste, np.array(recurso_destino_df_teste)]

            logging.info(f"Objeto preprocessado salvo.")

            salva_objeto(

                caminho_arquivo=self.configuracao_transformacao_dados.caminho_arquivo_obj_preprocessamento,
                obj=preprocessamento_obj

            )

            return (
                array_treino,
                array_teste,
                self.configuracao_transformacao_dados.caminho_arquivo_obj_preprocessamento,
            )
        except Exception as e:
            raise CustomException(e,sys)