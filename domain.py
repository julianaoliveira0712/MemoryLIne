from resoucers import *
import json
import pymongo

def allMemoryLine():
    cursor = conn.cursor()
    return json.dumps( cursor.execute('SELECT * from T_GAME;'))
    
client = pymongo.MongoClient("mongodb+srv://remember_auth:hRmXnjYiziGTz3DP@cluster0-d2d9w.azure.mongodb.net/test?retryWrites=true&w=majority")

    