import json
import tabulate as tabulate
import requests
import re
import os

def getAllGama():
    peticion = requests.get("http://172.16.100.118:5003")
    data = peticion.json()
    return data

#F