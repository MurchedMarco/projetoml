import sys
import pandas as pd
from src.exception import CustomException
from src.utils import carrega_objeto


class PipelinePredicao:
    def __init__(self):
        pass

    def predicao(self, recursos):
        try:
            caminho_modelo = 'artefatos/model.pkl'
            caminho_preprocessador = 'artefatos/preprocessamento.pkl'
            modelo = carrega_objeto(caminho_arquivo = caminho_modelo)
            preprocessamento = carrega_objeto(caminho_arquivo = caminho_preprocessador)
            dados_dimensionados = preprocessamento.transform(recursos)
            pred = modelo.predict(dados_dimensionados)

            return pred

        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(
            self,
            gender: str,
            race_ethnicity: str,
            parental_level_of_education,
            lunch: str,
            test_preparation_course: int,
            reading_score: int,
            writing_score: int
            ):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

        def obter_dados_df(self):
            try:
                custom_data_input_dict = {
                    "gender": [self.gender],
                    "race_ethnicity": [self.race_ethnicity],
                    "parental_level_of_education": [self.parental_level_of_education],
                    "lunch": [self.lunch],
                    "test_preparation_course": [self.   test_preparation_course],
                    "reading_score": [self.reading_score],
                    "writing_score": [self.writing_score],
                    }
                return pd.DataFrame(custom_data_input_dict)

            except Exception as e:
                raise CustomException(e, sys)