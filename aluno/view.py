from http import HTTPStatus

from flask import Flask, request

from aluno.service import AlunoService

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Bem vindo ao CRUD de aluno", HTTPStatus.OK


@app.route("/alunos", methods=['POST'])
def salvar():
    conteudo = request.json
    if conteudo is None:
        return "Json inválido", HTTPStatus.BAD_REQUEST
    try:
        aluno_service = AlunoService()
        aluno_service.salvar(conteudo)
        return "Registro salvo com sucesso", HTTPStatus.CREATED
    except Exception as e:
        return str(e), HTTPStatus.INTERNAL_SERVER_ERROR

app.run()