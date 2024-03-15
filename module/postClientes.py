import json
from tabulate import tabulate
import requests
import os

def getAllDatacliente():
     # json-server storage/cliente.json -b 5001
    peticioncli= requests.get("http://172.16.100.118:5001")
    datacli = peticioncli.json()
    return datacli


def postClientes():
        producto = {
        "codigo_cliente": int(input("Ingrese El codigo del cliente: ")),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido del contact: "),
        "telefono": int(input("Ingrese el Telefono: ")),
        "fax": int(input("Ingrese el fax")),
        "linea_direccion1": input("Ingrese la linea de direccion #1: "),
        "linea_direccion2": input("Ingrese la linea de direccion #2: "), 
        "ciudad": input("Ingrese la ciudad: "),
        "region": input("Ingrese la region: "),
        "pais": input("Ingrese el pais: "),
        "codigo_postal": int(input("Ingrese el codigo postal")),
        "codigo_empleado_rep_ventas": input("Ingrese el codigo del representante de ventas: "),
        "limite_credito": float(input("Ingrese el limite de credito:"))
        }