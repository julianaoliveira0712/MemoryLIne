from flask import Flask
from resoucers import *
from flask import json
from flask import request
from bson import json_util, ObjectId
from datetime import datetime
app = Flask(__name__)

# inserir uma nova memorie line
@app.route('/', methods = ['POST'])
def insertMemoryLine():
    headerRequest = request.headers.get("user_id")
    db.memoryLine.insert_one({
        "idOwner": headerRequest,  
        "participants": [],
        "creationDate": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "name": "maçã dourada"
    })
    response = {
        "success": True,
        "content": None,
        "erroData": None
    }
    return app.response_class(
        response = json.dumps(response, default = json_util.default),
        mimetype="application/json"
    )


# atualizar nome de uma memorie line
@app.route('/<id_memory_line>', methods = ['PUT'])
def updateMemoryLine(id_memory_line):
    headerRequest = request.headers.get("user_id")
    name = request.json
    db.memoryLine.find_one({ "_id" : ObjectId (id_memory_line)})

    db.memoryLine.update_one(
        {
             "_id" : ObjectId (id_memory_line)
        },
        {
            "$set": {
                "name": name
            }
        }
    )

    response = {
        "success": True,
        "content": None,
        "erroData": None
    }
    
    return app.response_class(
        response = json.dumps(response, default = json_util.default),
        mimetype="application/json"
    )

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

# db.pastel.insert_one({"author": "Mike",
#          "text": "My first blog post!",
#          "tags": ["mongodb", "python", "pymongo"]
#         })

    

# apagar uma nova memorie line
@app.route('/<id>', methods = ['DELETE'])
def deleteMemoryLine(id):
    db.memoryLine.delete_many({ "_id" : ObjectId (id)})
    return "Sucess"



# inserir uma moment numa memorie line
@app.route('/<id>', methods = ['POST'])
def insertmoment(id):
    query = db.memoryLine.find_one({ "_id" : ObjectId (id)})
    moment = request.json

    print(query)
    print(moment)

    query["moments"].append({
        "tituloMoment": moment["tituloMoment"],  
        "idMoment": moment["idMoment"],
        "tipo": moment["tipo"],
        "reacao": moment["reacao"],
        "comentarios": moment["comentarios"],
        "legenda": moment["legenda"],
        "dataCriacao": moment["dataCriacao"],
        "hora": moment["hora"]
    })

    db.memoryLine.update_one(
        {
             "_id" : ObjectId (id)
        },
        {
            "$set": {
                "moments": query["moments"]
            }
        }
    )
        
    return app.response_class(
            response= json.dumps(query, default = json_util.default),
            mimetype="application/json"
    )

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