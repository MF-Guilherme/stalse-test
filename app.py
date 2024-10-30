# importando o Flask para rodar o sistema e render_template para renderizar os templates
from flask import Flask, render_template
# importando o pandas para utilizar o DataFrame que já está criado
import pandas as pd

app = Flask(__name__)

# Movi para cima para melhorar a organização do código
# CRIANDO O DATAFRAME
df = pd.DataFrame(
    {
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
    }
)

@app.route('/')
def index():
    return render_template('index.html')

# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html (CRIE UM HTML PARA ISSO)
@app.route('/table')
def table():
    # convertendo o dataframe para html (no caso uma tabela)
    table_html = df.to_html(index=False, classes='table')
    # renderiando o template, passando a tabela html no contexto (para utilizar o Jinja2 no template)
    return render_template('table.html', table_html=table_html)

if __name__ == '__main__': # condicional para executar o programa somente se executado diretamente
    app.run(debug=True) # iniciando o servidor em modo debug para não precisar ficar reiniciando