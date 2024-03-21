import json
from tabulate import tabulate
import requests
import os 


def postOficinas():
    oficinas = {
        "codigo_oficina": input("Ingresa el codigo de la oficina: "),
        "ciudad": input("Ingresa la ciudad: "),
        "pais": input("Ingrese el  pais: "),
        "region": input("Ingresa la region: "),
        "codigo_postal": int(input("Ingresa el codigo postal")),
        "telefono": int(input("ingresa el telefono")),
        "linea_direccion1": input("ingresa la linea de direccion #1"),
        "linea_direccion2":input("ingresa la linea de direccion #2")
    
    }

    peticionoficina = requests.post("http://154.38.171.54:5005/oficinas", data=json.dumps(oficinas))
    res = peticionoficina.json()
    res["Mensaje"] = "Oficina guardada"
    return res

def deleteOfi(id):
    peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
    if peticion.status_code == 200:
        print("Oficina eliminado")



def menu():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                             ADMINISTRAR DATOS DE OFICINAS
                    
                                        ======================================
               

                        
               

                        1. Guardar oficina
                        2. Eliminar
                        0. Salir
               
""")
         
        opcion = int(input("Seleccione una opcion: "))
        if(opcion==1):
            print(tabulate(postOficinas(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            id = input("ingrese el id de la oficina que desea eliminar")
            print(deleteOfi(id))
        elif (opcion==0):
            break
                
