from flask import Flask, jsonify,request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Rafael',
      'habilidades' :['python', 'flask']},
    {'nome': 'Galleani',
     'habilibades': ['python', 'django']}
    ]

@app.route('/dev/<int:id>/', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem': 'registro excluido'})


@app.route('/dev/', methods = ['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'deu certo'})


if __name__ == '__main__':
    app.run()