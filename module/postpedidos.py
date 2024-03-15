import json
from tabulate import tabulate
import re
import requests
import os


def getAllDataPedidos():
     # json-server storage/pedido.json -b 5006
    peticionpedidos= requests.get("http://172.16.100.118:5006")
    datapedidos = peticionpedidos.json()
    return datapedidos

#D