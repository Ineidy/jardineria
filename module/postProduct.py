import json
import requests

def postProduct(producto):
    peticion = requests.post("http://172.16.100.115:5001", data=json.dumps(producto))

    res = peticion.json
    return peticion