from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos aneis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 1,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    }
]

#Get(all)
@app.route('/livros',methods=['GET'])
def get_livros():
    return jsonify(livros)

#Get(byId)
@app.route('/livros',methods=['GET'])
def get_livro_by_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#Put
@app.route('/livros/<int:id>',methods=['PUT'])
def edit_livros(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#Create
@app.route('/livros',methods=['POST'])
def include_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def exclude_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)        
        
app.run(port=3000,host='localhost',debug=True)