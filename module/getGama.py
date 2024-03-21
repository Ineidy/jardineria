
import requests
import os
from tabulate import tabulate

#json-server storage/gama_producto.json -b 5003

def getAllGama():
    peticiongama = requests.get("http://154.38.171.54:5004/")
    datagama = peticiongama.json()
    return datagama

def getAllNombre():
    gamanombre =[]
    for val in getAllGama():
        gamanombre.append(val.get("gama"))
    return gamanombre

