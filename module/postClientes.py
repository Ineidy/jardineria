import json
from tabulate import tabulate 
import requests
import os

def postClientes():
    clientes = {
        "codigo_cliente": int(input("Ingresa el codigo del cliente: ")),
        "nombre_cliente": input("ingresa el nombre del cliente: "),
        "nombre_contacto": input("ingresa el nombre del contacto: "),
        "apellido_contacto": input("Ingresa el apellido del contacto"),
        "telefono": int(input("ingresa el telefono: ")),
        "fax": int(input("Ingresa en fax del cliente: ")),
        "linea_direccion1": input("Ingresa la linea de direccion #1: "),
        "linea_direccion2": input("Ingresa la linea de direccion #2: "),
        "ciudad": input("Ingresa la ciudad: "),
        "region": input("ingresa la region: "),
        "pais": input("Ingresa el pais: "),
        "codigo_postal": int(input("Ingresa el codigo postal: ")),
        "codigo_empleado_rep_ventas": int(input("Ingresa de el representante de ventas: ")),
        "limite_credito": float(input("Ingresa el limite de credito: "))
    }

    posicionclientes = requests.post("http://192.168.10.159:5001", data=json.dumps(clientes))
    res = posicionclientes.json()
    res["Mensaje"] = "Cliente guardado"
    return res


def menu():
    while True: 
        os.system("clear")
        print("""

                                        ======================================

                                             ADMINISTRAR DATOS DE CLIENTES
                    
                                        ======================================
              


                        1. Guardar clientes
              
                        0. salir


""")
        
        opcion = int(input("Seleccione una opcion: "))
        if(opcion==1):
            print(tabulate(postClientes(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==0):
            break