import json
from tabulate import tabulate
import re
import requests
import os

def getAllDataPago():
     # json-server storage/pago.json -b 5005
    peticionpago= requests.get("http://172.16.100.118:5005")
    datapago = peticionpago.json()
    return datapago
