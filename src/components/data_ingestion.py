import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import TransformacaoDados
from src.components.data_transformation import ConfiguracaoTransformacaoDados

import pandas as pd
from sklearn.model_selection import train_test_split




@dataclass
class ConfiguracaoIngestaoDados:
    caminho_dados_treino: str = os.path.join('artefatos', "train.csv")
    caminho_dados_teste: str = os.path.join('artefatos', "test.csv")
    caminho_dados_cru: str = os.path.join('artefatos', "data.csv")

class IngestaoDados:
    def __init__(self):
        self.configuracao_ingestao = ConfiguracaoIngestaoDados()

    def inicia_ingestao_dados(self):
        logging.info("Insira o método ou componente de ingestão de dados")
        try:
            df = pd.read_csv(os.path.join('notebook', 'data', 'stud.csv'))
            logging.info('Conjunto de dados lido como dataframe')

            os.makedirs(os.path.dirname(self.configuracao_ingestao.caminho_dados_treino), exist_ok=True)

            df.to_csv(self.configuracao_ingestao.caminho_dados_cru, index=False, header=True)

            logging.info("Train test split iniciado")
            conjunto_treino, conjunto_teste = train_test_split(df, test_size=0.2, random_state=42)

            conjunto_treino.to_csv(self.configuracao_ingestao.caminho_dados_treino, index=False, header=True)

            conjunto_teste.to_csv(self.configuracao_ingestao.caminho_dados_teste, index=False, header=True)

            logging.info("Ingestão dos dados completa.")

            return (
                self.configuracao_ingestao.caminho_dados_treino,
                self.configuracao_ingestao.caminho_dados_teste
            )
        except Exception as e:
            logging.error(f":Ocorreu um erro durante a ingestão de dados {str(e)}.")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = IngestaoDados()
    dados_treino, dados_teste = obj.inicia_ingestao_dados()

    transformacao_dados = TransformacaoDados()
    transformacao_dados.inicia_transformacao_dados(dados_treino, dados_teste)
