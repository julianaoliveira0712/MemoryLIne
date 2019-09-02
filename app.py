from flask import Flask
from resoucers import *
from flask import json
from flask import request
from bson import json_util, ObjectId
app = Flask(__name__)

# listar as memory line 

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
    query = db.memoryLine.find_one({ "_id" : ObjectId (id)})
    
    return app.response_class(
        response= json.dumps(query, default = json_util.default),
        mimetype="application/json"
            
    )

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
    db.memoryLine.delete_many({ "_id" : ObjectId (id)})
    return "Sucess"

# atualizar nome de uma memorie line
@app.route('/<id>', methods = ['PUT'])
def updateMemoryLine(id):
    return "1"

# inserir uma moment numa memorie line
@app.route('/<id>', methods = ['POST'])
def insertmoment(id):
    query = db.memoryLine.find_one({ "_id" : ObjectId (id)})
    db.query.update_many(
    { },
    { $set: { moment: new moments } }
    )
    
    moment = request.json
    db.memoryLine.moment.insert_one({
        "tituloMoment": moment["tituloMoment"],  
        "idMoment": moment["idMoment"],
        "tipo": moment["tipo"],
        "reacao": moment["reacao"],
        "comentarios": moment["comentario"],
        "legenda": moment["legenda"],
        "dataCriacao": moment["data"],
        "hora": hora["hora"]
    })

    return app.response_class(
            response= json.dumps(query, default = json_util.default),
            mimetype="application/json"

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