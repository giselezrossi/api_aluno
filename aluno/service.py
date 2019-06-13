from aluno.model import Aluno


class AlunoService():

    def salvar(self, dict_data):
        name = dict_data['nome']
        if not name:
            raise Exception("sfsfg")
        #salvar no mongo
        pass