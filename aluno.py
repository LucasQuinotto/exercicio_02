from flask import request, json
from bson.objectid import ObjectId
from pandas import pandas as pd


class Aluno:

    def consultar_provas(self, prova):
        df = pd.DataFrame(prova.find())
        df = df.drop(['questoes'], axis=1)
        df = df.astype(str)
        return df.to_json(orient="records")

    def consultar_prova_questoes(self, prova):
        raw_request = request.data.decode("utf-8")
        dict_values = json.loads(raw_request)
        try:
            dicio = list(prova.find({'_id': ObjectId(dict_values['_id'])}))
        except:
            return "Esta prova não foi encontrada ..."

        for values in dicio[0]['questoes']:
            values.pop('correta')
        df = pd.DataFrame(dicio)
        df = df.drop(['_id'], axis=1)
        return df.to_json(orient="records")

    def fazer_prova(self, prova, aluno, gabarito=[], peso_questao=[], nota_final=0.0):
        raw_request = request.data.decode("utf-8")
        dict_values = json.loads(raw_request)

        try:
            dicio = list(prova.find({'_id': ObjectId(dict_values['id_prova'])}))
            aluno.find({'_id': ObjectId(dict_values['id_matricula'])})
        except:
            return "O id da prova ou Aluno(a) está incorreto ...", 400

        for values in dicio[0]['questoes']:
            gabarito.append(values['correta'])
            peso_questao.append(values['peso'])

        try:
            for i in range(len(dicio[0]['questoes'])):
                if dict_values[f'{i + 1}'] == gabarito[i]:
                    nota_final += peso_questao[i]
            return f"dale rapaz, sua nota final é {nota_final}"
        except:
            return "o numero das questões não corresponde ao gabarito ...", 400


