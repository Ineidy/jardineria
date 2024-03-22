import json
from tabulate import tabulate
import requests
import os


def postPagos():
    pagos = {
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingresa el id de la transaccion: "),
        "fecha_pago": input("Ingresa una fecha de pago: "),
        "total": int(input("Ingresa el total del pago: "))
    }

    peticionpago = requests.post("http://154.38.171.54:5006/pagos", data=json.dumps(pagos))
    res=peticionpago.json()
    res["Mensaje"] = "Pago guardado"
    return res 

def getAllDataPago():
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data

def deletepago(id):
    peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
    if peticion.status_code == 200:
        print("pago eliminado")



def menu():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                             ADMINISTRAR DATOS DE PAGOS
                    
                                        ======================================
              


              
                        1. Guadar pago
                        2. Eliminar
                        0.salir
""")
        
        opcion = int(input("Selecione una opcion: "))
        if(opcion==1):
            print(tabulate(postPagos(),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            id = input("Ingrese el id del pago que desea eliminar")
            print(deletepago(id))
        elif(opcion==2):
            break