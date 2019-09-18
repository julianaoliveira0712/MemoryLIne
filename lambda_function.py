import json
import pymongo
from bson import json_util, ObjectId

client = pymongo.MongoClient("mongodb+srv://remember_auth:hRmXnjYiziGTz3DP@cluster0-d2d9w.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client["remember-dev"]

def lambda_handler(event, context):
    # TODO implement
    
    memoryLines=[]
    query = db.memoryLine.find()
    for row in query:
        memoryLines.append(row)
        
    
    return {
        'statusCode': 200,
        'body': json.dumps(memoryLines, default = json_util.default)
    }
