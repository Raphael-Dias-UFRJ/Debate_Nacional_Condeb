from flask import Flask, render_template, request , redirect ,url_for
from tinydb import TinyDB, Query
import random

app = Flask(__name__)
bd = TinyDB('debatedores.json')

class Debatedor:
    def __init__(self, nome_sd,dupla_sd) -> None:
        self.nome_sd = nome_sd
        self.dupla_sd = dupla_sd

@app.route('/')
def index():
    bd.clear_cache()
    debatedores = bd.all()
    return render_template('index.html', debatedores=debatedores)

@app.route('/', methods = ['POST'])
def enviar():
    nome_sd = request.form.get('nome_sd')
    dupla_sd = request.form.get('dupla_sd')
    c = Debatedor(nome_sd,dupla_sd)
    bd.insert({"nome_sd": c.nome_sd, "dupla_sd": c.dupla_sd})
    bd.clear_cache()
    return redirect(url_for('index'))


'''@app.route("/delete/<nome_sd>")
def delete(nome_sd):
    delete debater 
    nome_sd = Query()
    bd.update(delete('nome_sd','dupla_sd'), where('nome_sd') == nome_sd)
    return redirect(url_for("index"))'''


if __name__ == '__main__':
    app.run(debug = True)