from flask import Flask
from resoucers import *
from flask import json
from flask import request
from bson import json_util
app = Flask(__name__)


@app.route('/all')
def getAllMemoryLine():
    memoryLines=[]
    query = db.memoryLine.find()
    for row in query:
        memoryLines.append(row)
        print(row)
    
    return app.response_class(
        response= json.dumps(memoryLines, default = json_util.default),
        mimetype="application/json"
    )

# pegar uma memory line especifica
@app.route('/<id>')
def getSpecificMemoryLine(id):
    return "1"

# inserir uma nova memorie line
@app.route('/', methods = ['POST'])
def insertMemoryLine():
    dadosPedido = request.json
    db.memoryLine.insert_one({
        "nomeMemorieline": dadosPedido["nomeMemorieline"],  
        "participantes": dadosPedido["participantes"],
        "moments": dadosPedido["moments"],
        "dataCriacao": dadosPedido["dataCriacao"]
    })
    return "Sucess"

# db.pastel.insert_one({"author": "Mike",
#          "text": "My first blog post!",
#          "tags": ["mongodb", "python", "pymongo"]
#         })

    

# apagar uma nova memorie line
@app.route('/<id>', methods = ['DELETE'])
def deleteMemoryLine(id):
    return "1"

# atualizar nome de uma memorie line
@app.route('/<id>', methods = ['PUT'])
def updateMemoryLine(id):
    return "1"

# inserir uma moment numa memorie line
@app.route('/<id>/<idmoment>', methods = ['POST'])
def insertmoment(id,idmoment):
    return "1"

# deletar uma moment de uma memorie line
@app.route('/<id>/<idmoment>', methods = ['DELETE'])
def deletemoment(id, idmoment):
    return "1"

# atualizar um moment
@app.route('/<id>/<idmoment>', methods = ['PUT'])
def updateMoments(id,idmoment):
    return "1"

# compartilhar time line
@app.route('/<id>/share')
def shareMemoryLine(id):
    return "1"

# convidar amigo
@app.route('/<id>/invite/<iduser>')
def inviteFriend(id,iduser):
    return id+iduser



