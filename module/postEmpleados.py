import json
from tabulate import tabulate 
import re
import requests
import os


def getAllDataEmpleados():
     # json-server storage/empleado.json -b 5002
    peticionEmple= requests.get("http://172.16.100.118:5002")
    dataEmple = peticionEmple.json()
    return dataEmple
