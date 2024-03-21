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

    peticionpedi = requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(pedidos))
    res = peticionpedi.json()
    res["Mensaje"] = "Pedido guardado"
    return res

def deletepedido(id):
    peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
    if peticion.status_code == 200:
        print("pedido eliminado")



def menu():
    while True:
        os.system("clear")
        print("""


                                        ======================================

                                             ADMINISTRAR DATOS DE PEDIDOS
                    
                                        ======================================
              

              


                            1. Guardar datos de pedidos
                            2. Eliminar
                            0. Salir
              
""")

        opcion = int(input("Seleccione Una opcion: "))
        if(opcion==1):
            print(tabulate(postPedidos(), headers="keys", tablefmt='rounded_grid'))
            print("Oprima una tecla para continuar........")
        elif(opcion==2):
            id = input("Ingrese el id del pedido que desea eliminar")
            print(deletepedido(id))
        elif(opcion==0):
            break