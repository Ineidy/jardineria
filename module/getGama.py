
import requests
import os
from tabulate import tabulate

#json-server storage/gama_producto.json -b 5003

def getAllGama():
    peticion = requests.get("http://172.16.100.118:5003")
    data = peticion.json()
    return data

def getAllNombre():
    gamanombre =[]
    for val in getAllGama():
        gamanombre.append(val.get("gama"))
    return gamanombre
