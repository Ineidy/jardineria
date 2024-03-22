import json
from tabulate import tabulate 
import requests
import os
import module.getClients as reportesclientes

def postCliente():
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

    posicionclientes = requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(clientes))
    res = posicionclientes.json()
    res["Mensaje"] = "Cliente guardado"
    return res

def getAllDataClientes():
    peticionesclientes = requests.get("http://154.38.171.54:5001/cliente")
    dataclientes = peticionesclientes.json()
    return dataclientes 

def deleteCliente(id):
    peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
    if peticion.status_code == 200:
        print("Cliente eliminaresdo")


# def eliminarCliente(id):
#     data = reportesclientes.getClienteCodigo(id)
#     if(len(data)):
#         peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
#         if(peticion.status_code == 204):
#             data.append({"message": "producto eliminado correctamente"})
#             return {
#                 "body": data, 
#                 "status": peticion.status_code,
#             }
#     else:
#         return {
#             "body":[{
#                 "message":"producto no encontrado",
#                 "id": id
#             }],
#             "status": 400,
#         }

def menu():
    while True: 
        print("""

                                        ======================================

                                             ADMINISTRAR DATOS DE CLIENTES
                    
                                        ======================================
              


                        1. Guardar clientes
              
                        2. Eliminar clientes
              
                        0. salir


""")
        
        opcion = int(input("Seleccione una opcion: "))
        if(opcion==1):
            print(tabulate(postCliente(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            id = input("Ingrese el id de el cliente que desea eliminar")
            print(deleteCliente(id))
        elif(opcion==0):
            break    # json-server storage/producto.json -b 5007
        # peticion = requests.post("http://154.38.171.54:5007", data=json.dumps(producto))
        # res = peticion.json()
        # res["Mensaje"] = "Producto Guardado"
        # return [res]