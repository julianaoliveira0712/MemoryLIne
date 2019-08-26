from flask import Flask
from domain import *
app = Flask(__name__)


@app.route('/all')
def getAllMemoryLine():
    return allMemoryLine()

# pegar uma memory line especifica
@app.route('/<id>')
def getSpecificMemoryLine(id):
    return "1"

# inserir uma nova memorie line
@app.route('/', methods = ['POST'])
def insertMemoryLine():
    return "1"

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

