from flask import request, json


class Professor():

    def matricular_aluno(self, aluno):
        raw_request = request.data.decode("utf-8")
        dict_values = json.loads(raw_request)
        aluno.insert_one(dict_values)
        return f"o(a) {dict_values['nome']} foi matriculado(a) com sucesso!!"

    def cadastrar_prova(self, prova, numero_questao=0, peso_total=0):
        raw_request = request.data.decode("utf-8")
        dict_values = json.loads(raw_request)

        if len(dict_values['questoes']) >= 1 and len(dict_values['questoes']) <= 20:
            for dict_questoes in dict_values['questoes']:
                numero_questao += 1
                dict_questoes['numero'] = numero_questao
                if dict_questoes['peso'] > 0.001:
                    peso_total += dict_questoes['peso']
                else:
                    return "nenhuma questão pode ter peso menor que 0.001 :(", 400

            if peso_total != 10.0:
                return f"o peso final da prova deve ser 10.0 ... , peso atual: {peso_total}", 400
            else:
                prova.insert_one(dict_values)
                return f"a prova foi cadastrada com sucesso !!", 200
        else:
            return f"a prova deve conter entre 1 e 20 questões ..., e esta tem{len(dict_values['questoes'])} questoes :(", 400
