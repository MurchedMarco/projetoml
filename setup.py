from setuptools import find_packages,setup
from typing import List

HIFEN_E_PONTO='-e .'
def obter_requisitos(caminho_arquivo:str)->List[str]:
    '''
    Essa função retorna a lista de requesitos
    '''
    requerimentos=[]
    with open(caminho_arquivo) as arq_obj:
        requerimentos=arq_obj.readlines()
        requerimentos=[req.replace("\n","") for req in requerimentos]

        if HIFEN_E_PONTO in requerimentos:
            requerimentos.remove(HIFEN_E_PONTO)
    
    return requerimentos

setup(
name='mlproject',
version='0.0.1',
author='MurchedMarco',
author_email='euocram@gmail.com',
packages=find_packages(),
install_requires=obter_requisitos('requirements.txt')

)