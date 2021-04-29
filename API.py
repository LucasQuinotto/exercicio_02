from flask import Flask
import pymongo
from aluno import Aluno
from professor import Professor


app = Flask(__name__)


@app.route("/professor/matricular_aluno/", methods=["POST"])
def matricular_aluno():
    return Professor().matricular_aluno(aluno)

@app.route("/professor/cadastrar_prova/", methods=["POST"])
def cadastrar_prova():
    return Professor().cadastrar_prova(prova)

@app.route("/aluno/consultar_provas/")
def consultar_provas():
    return Aluno().consultar_provas(prova)

@app.route("/aluno/consultar_questoes_prova/", methods=["POST"])
def consultar_prova_questoes():
    return Aluno().consultar_prova_questoes(prova)

@app.route("/fazer_provas/", methods=["POST"])
def fazer_prova():
    return Aluno().fazer_prova(prova, aluno)


conexao = pymongo.MongoClient("mongodb://localhost:27017/")['exercicio_02']

aluno = conexao['aluno']
prova = conexao['prova']


if __name__ == "__main__":
    app.run(debug=True)