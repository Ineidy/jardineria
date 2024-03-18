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

    peticionoficina = requests.post("http://192.168.10.159:5004", data=json.dumps(oficinas))
    res = peticionoficina.json()
    res["Mensaje"] = "Oficina guardada"
    return res



def menu():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                             ADMINISTRAR DATOS DE OFICINAS
                    
                                        ======================================
               

                        
               

                        1. Guardar oficina
               
                        0. Salir
               
""")
         
        opcion = int(input("Seleccione una opcion: "))
        if(opcion==1):
            print(tabulate(postOficinas(), headers="keys", tablefmt='rounded_grid'))
        elif (opcion==0):
            break
                
