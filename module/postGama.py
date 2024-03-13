import json
import requests

#json-server storage/gama_producto.json -b 5002

def getAllGama():
    peticion = requests.get("f")
    data = peticion.json()
    return data
