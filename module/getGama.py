
import requests

#json-server storage/gama_producto.json -b 5002

def getAllGama():
    peticion = requests.get("http://172.16.100.118:5002")
    data = peticion.json()
    return data

def getAllNombre():
    gamanombre =[]
    for val in getAllGama():
        gamanombre.append(val.get("gama"))
    return gamanombre
