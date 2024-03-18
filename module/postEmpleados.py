import json
from tabulate import tabulate
import requests
import os


def postEmpleados():
    empleados = {
        "codigo_empleado": int(input("Ingresa el codigo de empleado: ")),
        "nombre": input("Ingresa el nombre del empleado: "),
        "apellido1": input("Ingresa el primer apellido del empleado: "),
        "apellido2": input("Ingresa el segundo apellido del empleado: "),
        "extension": int(input("ingresa la extension del empleado")),
        "email": input("Igresa el email: "),
        "codigo_oficina": input("Ingresa el codigo de la oficina: "),
        "codigo_jefe": input("Ingresa el codigo del jefe: "),
        "puesto": input("Ingresa el puesto del empleado: ")
    }

    peticionempleado = requests.post("http://192.168.10.159:5002", data=json.dumps(empleados))
    res = peticionempleado.json()
    res["Mensaje"] = "Empleado Guardado"
    return res


def menu():
    while True: 
        os.system("clear")
        print("""

                                        ======================================

                                            ADMINISTRAR DATOS DE EMPLEADOS
                    
                                        ======================================
               
              


                        1. Guardar empleado
              
                        0. Salir

""")
        
        opcion = int(input("Seleccione una opcion: "))
        if(opcion==1):
            print(tabulate(postEmpleados(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==0):
            break 
    