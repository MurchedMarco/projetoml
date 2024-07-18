import sys
import logging

logging.basicConfig(level=logging.INFO)

def error_message_detail(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Ocorreu um erro no seu script Python.\nO nome do erro é [{0}], na linha número [{1}] com a mensagem de erro[{2}]'.format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomExcepition(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details=sys)

    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('Não pode dividir por ZERO.')
        raise CustomExcepition(str(e))
