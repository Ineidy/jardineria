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

    peticionpago = requests.post("http://192.168.10.159:5005", data=json.dumps(pagos))
    res=peticionpago.json()
    res["Mensaje"] = "Pago guardado"
    return res 




def menu():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                             ADMINISTRAR DATOS DE PAGOS
                    
                                        ======================================
              


              
                        1. Guadar pago
              
                        0.salir
""")
        
        opcion = int(input("Selecione una opcion: "))
        if(opcion==1):
            print(tabulate(postPagos(),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            break