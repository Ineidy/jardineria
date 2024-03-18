import json
from tabulate import tabulate
import requests
import os



def postPedidos():
    pedidos = {
        
        "codigo_pedido": int(input("Ingrese el codigo del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha esperada: "),
        "fecha_entrega": input("Ingrese la fecha de entrega del pedido: "),
        "estado": input("Ingrese el estado sel pedido: "),
        "comentario": input("Ingrese Un comentario: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
    }

    peticionpedi = requests.post("http://192.168.10.159:5006", data=json.dumps(pedidos))
    res = peticionpedi.json()
    res["Mensaje"] = "Pedido guardado"
    return res



def menu():
    while True:
        os.system("clear")
        print("""


                                        ======================================

                                             ADMINISTRAR DATOS DE PEDIDOS
                    
                                        ======================================
              

              


                            1. Guardar datos de pedidos
              
                            0. Salir
              
""")

        opcion = int(input("Seleccione Una opcion: "))
        if(opcion==1):
            print(tabulate(postPedidos(), headers="keys", tablefmt='rounded_grid'))
            print("Oprima una tecla para continuar........")
        elif(opcion==0):
            break