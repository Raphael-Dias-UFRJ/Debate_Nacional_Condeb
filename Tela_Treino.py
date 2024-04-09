from flask import Flask, render_template
from flask.globals import request
from tinydb import TinyDB, Query

app = Flask(__name__)
bd = TinyDB('debatedores.json')

@app.route('/')
def index():
    bd.clear_cache()
    return render_template('index.html',
    debatedores = bd.all())

@app.route('/', methods = ['POST'])
def enviar():
    c = debatedor.Debatedor(nome_sd = request.form['nome_sd'],
                            dupla_sd = request.form['dupla_sd'])

    bd.insert({"nome_sd": c.nome_sd, "dupla_sd": c.dupla_sd})
    bd.clear_cache()

if __name__ == '__main__':
    app.run(debug = True)