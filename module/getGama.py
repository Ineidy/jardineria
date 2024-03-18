
import requests
import os
from tabulate import tabulate

#json-server storage/gama_producto.json -b 5003

def getAllGama():
    peticiongama = requests.get("http://192.168.10.159:5003")
    datagama = peticiongama.json()
    return datagama

def getAllNombre():
    gamanombre =[]
    for val in getAllGama():
        gamanombre.append(val.get("gama"))
    return gamanombre

