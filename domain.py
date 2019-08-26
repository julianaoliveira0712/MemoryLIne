from resoucers import *
import json

def allMemoryLine():
    cursor = conn.cursor()
    return json.dumps( cursor.execute('SELECT * from T_GAME;'))
    

    