from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PipelinePredicao

aplicacao = Flask(__name__)

app = aplicacao

# Rota pra a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prever_dados', methods = ['GET', 'POST'])
def prever_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        dados = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )

        df_pred = dados.obter_dados_df()
        print(df_pred)
        print('Antes da predição')

        pipeline_predicao = PipelinePredicao()
        print("Meio da predição")
        resultados = pipeline_predicao.predicao(df_pred)
        print("Após a predição")

        return render_template('home.html', resultados = resultados[0])
    
    if __name__ == '__main__':
        #app.run(host = '0.0.0.0', debug = True)
        #app.run(debug = True)
        app.run(debug=True, port=5000)

print('http://127.0.0.1:5000/prever_dados')
