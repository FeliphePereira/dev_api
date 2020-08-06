from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json
app = Flask(__name__)
api = Api(app)
desenvolvedores = [
    {'nome':'Rafael',
      'habilidades' :['python', 'flask']},

    {'nome': 'Galleani',
     'habilibades': ['python', 'django']}]
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','nebsagem':mensagem}
        return jsonify(response)

    def put(self):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)