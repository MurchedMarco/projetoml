import sys
from src.logger import logging

def detalhes_mensagem_erro(erro,detalhe_erro:sys):
    _,_,exc_tb=detalhe_erro.exc_info()
    nome_arquivo=exc_tb.tb_frame.f_code.co_filename
    erro_menssagem="erro ocorreu no script [{0}] número da linha [{1}] mensagem de erro [{2}]".format(
     nome_arquivo,exc_tb.tb_lineno,str(erro))

    return erro_menssagem

    

class CustomException(Exception):
    def __init__(self,erro_menssagem,detalhe_erro:sys):
        super().__init__(erro_menssagem)
        self.erro_menssagem=detalhes_mensagem_erro(erro_menssagem,detalhe_erro=detalhe_erro)
    
    def __str__(self):
        return self.erro_menssagem
    


        