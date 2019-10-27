from flask import Flask
from resoucers import *
from flask import json
from flask import request
from bson import json_util, ObjectId
from datetime import datetime
app = Flask(__name__)

# inserir uma nova memorie line
@app.route('/', methods=['POST'])
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
        response=json.dumps(response, default=json_util.default),
        mimetype="application/json"
    )


# atualizar nome de uma memorie line
@app.route('/<id_memory_line>', methods=['PUT'])
def updateMemoryLine(id_memory_line):
    headerRequest = request.headers.get("user_id")
    name = request.json
    memory = db.memoryLine.find_one({"_id": ObjectId(id_memory_line)})
    response = {
        "success": False,
        "content": None,
        "erroData": {
            "typeError": "Unathourized",
            "message": "reação ou usuário inexistente"
        }
    }
    if(memory == None or memory["idOwner"] != headerRequest):
        return app.response_class(
            response=json.dumps(response, default=json_util.default),
            mimetype="application/json"
        )
    else:
        db.memoryLine.update_one(
            {
                "_id": ObjectId(id_memory_line)
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
        response=json.dumps(response, default=json_util.default),
        mimetype="application/json"
    )

    # for row in query:
    #     id = str(row["_id"])
    #     memoryLines.append({
    #         "idMemoryLine": id,
    #         "creationDate":
    #     })

    # return app.response_class(
    #     response= json.dumps(memoryLines, default = json_util.default),
    #     mimetype="application/json"
    # )

# listar as memory line
@app.route('/all', methods=['GET'])
def getmemoryLine():
    headerRequest = request.headers.get("user_id")
    query = db.memoryLine.find({"idOwner": headerRequest})
    memoryLinePublic = []
    memoryLinePrivate = []
    for row in query:
        id = str(row["_id"])
        if(len(row['participants']) == 0):
            memoryLinePrivate.append({
                "idMemoryLine": id,
                "idOwner": row['idOwner'],
                "quantityParticipants": len(row['participants']),
                "creationDate": row['creationDate'],
                "name": row['name']
            })
        else:
            memoryLinePublic.append({
                "idMemoryLine": id,
                "idOwner": row['idOwner'],
                "quantityParticipants": len(row['participants']),
                "creationDate": row['creationDate'],
                "name": row['name']
            })

    response = {
        "success": True,
        "content": {
            "private": memoryLinePrivate,
            "public": memoryLinePublic
        },
        "erroData": None
    }
    return app.response_class(
        response=json.dumps(response, default=json_util.default),
        mimetype="application/json"
    )

# # pegar uma memory line especifica
# @app.route('id_memoryLine>', methods = ['GET'])
# def getSpecificMemoryLine(id_memoryLine):
#     headerRequest =request.headers.get("user_id")
#     query = db.memoryLine.find_one({ "_id" : ObjectId (id_memoryLine)})
#     if(query == None):
#         response = {
#         "success": False,
#         "content": None,
#         "erroData": {
#         "typeError": "Unathourized",
#         "message": "reação ou usuário inexistente"
#         }
#     }
#     else:
#         memory = {
#             "idOwner": query['idOwner'],
#             "participants": query['participantes'],
#             "creationDate": query['creationDate'],
#             "name": query['name']
#         })
#             }
#         response = {
#             "success": True,
#             "content": memory,
#             "erroData": None
#         }
#         return app.response_class(
#             response = json.dumps(response, default = json_util.default),
#             mimetype="application/json"
#         )

# apagar uma nova memory line
@app.route('/memory-line/<id_memoryLine>', methods=['DELETE'])
def deleteMemoryLine(id_memoryLine):
    headerRequest = request.headers.get("user_id")
    memoryLine = db.memoryLine.find_one({"_id": ObjectId(id_memoryLine)})
    response = {
        "success": False,
        "content": None,
        "erroData": {
            "typeError": "Unathourized",
            "message": "Moment não existe ou usuário não existe"
        }
    }

    if(memoryLine == None or memoryLine["idOwner"] != headerRequest):
        return app.response_class(
            response=json.dumps(response, default=json_util.default),
            mimetype="application/json"
        )
    else:
        db.memoryLine.delete_one({"_id": ObjectId(id_memoryLine)})
        response = {
            "success": True,
            "content": None,
            "erroData": None
        }
        return app.response_class(
            response=json.dumps(response, default=json_util.default),
            mimetype="application/json"
        )


@app.route('/memory-line/<id_memory_line>/<id_profile>', methods=['POST'])
def inviteUser(id_memory_line, id_profile):
    headerRequest = 'ec8aad84-2150-495b-8a00-734c21f69619'

    query = db.invites.find_one({
        "idOwner": headerRequest,
        "idReceiver": id_profile,
        "idMemoryLine": id_memory_line,
        "answer": True,
        "accepted": True
    })

    response = {
        "success": True,
        "content": None,
        "erroData": None
    }

    if(query != None):
        response = {
            "success": False,
            "content": None,
            "erroData": {
                "typeError": "Unathourized",
                "message": "Já está na Memory Line"
            }
        }
    else:
        query = db.invites.find_one({
            "idOwner": headerRequest,
            "idReceiver": id_profile,
            "idMemoryLine": id_memory_line,
            "answer": False
        })
        if(query != None):
            response = {
                "success": False,
                "content": None,
                "erroData": {
                    "typeError": "Unathourized",
                    "message": "Possui convite pendente."
                }
            }
        else:
            db.invites.insert_one({
                "idOwner": headerRequest,
                "idReceiver": id_profile,
                "idMemoryLine": id_memory_line,
                "answer": False,
                "accepted": False,
                "creationDate": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            })

    return app.response_class(
        response=json.dumps(response, default=json_util.default),
        mimetype="application/json"
    )

@app.route('/memory-line/invites', methods=['GET'])
def invites():
    headerRequest = 'ec8aad84-2150-495b-8a00-734c21f69619'
    query = db.invites.find({
        "idReceiver": headerRequest,
        "answer": False
    })

    invites = []
    for row in query:
        id = str(row["_id"])
        memoryLine = db.memoryLine.find_one(
            {"_id": ObjectId(row['idMemoryLine'])})

        invites.append({
            "idInvite": id,
            "idOwner": row['idOwner'],
            "idReceiver": headerRequest,
            "idMemoryLine": row['idMemoryLine'],
            "nameMemoryLine": memoryLine['name'],
            "participants": len(row['participants']),
            "answer": False,
            "accepted": False,
            "creationDate": row['creationDate']
        })

    response = {
        "success": True,
        "content": invites,
        "erroData": None
    }
    return app.response_class(
        response=json.dumps(response, default=json_util.default),
        mimetype="application/json"
    )

@app.route('/memory-line/invites/<id_invite>', methods=['PUT'])
def answerInvite(id_invite):
    answer = request.json
    headerRequest = 'ec8aad84-2150-495b-8a00-734c21f69619'

    query = db.invites.find_one({
        "_id": ObjectId(id_invite),
        "answer": False,
        "idReceiver": headerRequest
    })

    response = {
        "success": True,
        "content": None,
        "erroData": None
    }

    if(query == None):
        response = {
            "success": False,
            "content": None,
            "erroData": {
                "typeError": "Unathourized",
                "message": "Convite inválido"
            }
        }
    else:
        db.invites.update_one(
            {
                "_id": ObjectId(id_invite)
            },
            {
                "$set": {
                    "answer": True,
                    "accepted": answer
                }
            }
        )
        if(answer == True):
            memoryLine = db.memoryLine.find_one({
                "_id": ObjectId(query["idMemoryLine"])
            })

            participants = []

            for participant in memoryLine["participants"]:
                participants.append(participant)

            participants.append(headerRequest)

            db.memoryLine.update_one(
                {
                    "_id": ObjectId(query["idMemoryLine"])
                },
                {
                    "$set": {
                        "participants": participants
                    }
                }
            )

    return app.response_class(
        response=json.dumps(response, default=json_util.default),
        mimetype="application/json"
    )


# # compartilhar uma memory line
# @app.route('/<id>/share')
# def shareMemoryLine(id):
#     return "1"

# # convidar amigo para uma memory Line
# @app.route('/<id>/invite/<iduser>')
# def inviteFriend(id,iduser):
#     return id+iduser

# deletar memoryLine (antigo)
# @app.route('/<id>', methods = ['DELETE'])
# def deleteMemoryLine(id):
   # db.memoryLine.delete_many({ "_id" : ObjectId (id)})
   # return "Sucess"

# teste de insert no banco
# db.pastel.insert_one({"author": "Mike",
#          "text": "My first blog post!",
#          "tags": ["mongodb", "python", "pymongo"]
#         })

# pegar uma memoryLine especifica (antigo)
# @app.route('/<id>')
# def getSpecificMemoryLine(id):
#   query = db.memoryLine.find_one({ "_id" : ObjectId (id)})
#  return app.response_class(
#       response= json.dumps(query, default = json_util.default),
#      mimetype="application/json"
# )

# Pegar todas memoryLIne (antigo)
# @app.route('/all')
# def getAllMemoryLine():
#   memoryLines=[]
#   query = db.memoryLine.find()
#   for row in query:
#       memoryLines.append(row)
#       print(row)
#
#   return app.response_class(
#       response= json.dumps(memoryLines, default = json_util.default),
#       mimetype="application/json"
#    )
