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

    peticionempleado = requests.post("http://154.38.171.54:5003/empleados", data=json.dumps(empleados))
    res = peticionempleado.json()
    res["Mensaje"] = "Empleado Guardado"
    return res       

def getAllDataEmpleados():
    peticionesempleados = requests.get("http://154.38.171.54:5003/empleados")
    dataempleados = peticionesempleados.json()
    return dataempleados


def deleteEmple(id):
    peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
    if peticion.status_code == 200:
        print("Empleado eliminado")

def menu():
    while True: 
        os.system("clear")
        print("""

                                        ======================================

                                            ADMINISTRAR DATOS DE EMPLEADOS
                    
                                        ======================================
               
              


                        1. Guardar empleado
              
                        2. Eliminar
              
                        0. Salir

""")
        
        opcion = int(input("Seleccione una opcion: "))
        if(opcion==1):
            print(tabulate(postEmpleados(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            id = input("Ingrese el id de el empleado que desea eliminar")
            print(deleteEmple(id))
        elif(opcion==0):
            break 
    