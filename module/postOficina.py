import json
from tabulate import tabulate
import re
import requests


def getAllDataoficina():
     # json-server storage/oficina.json -b 5004
    peticionofi= requests.get("http://172.16.100.118:5004")
    dataofi = peticionofi.json()
    return dataofi
