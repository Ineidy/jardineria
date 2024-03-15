
from tabulate import tabulate
import os
import requests


def getAllDataEmpleados():
     # json-server storage/empleado.json -b 5002
    peticionEmple= requests.get("http://172.16.100.118:5002")
    dataEmple = peticionEmple.json()
    return dataEmple


# empleados con jefe de codigo 7 
def getAllNombreApellidoEmailJefeNum7():
    nombreApellidoEmail =[]
    for val in getAllDataEmpleados():
        if (val.get("codigo_jefe") == 7):
            nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": F'{val.get("apellido1")}{val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail

#info de los que no son representantes de ventas.
def getAllNombreApellidoPuesto():
    nombreApellidoPuesto =[]
    for val in getAllDataEmpleados():
        if (val.get("puesto") != ("Representante Ventas")):
            nombreApellidoPuesto.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                    "puesto": val.get("puesto")
                }
            )

    return nombreApellidoPuesto

#nombre del puesto, nombre, apellidos y email del jefe de la empresa

def getAllNombreApellidoEmailJefe():
    nombreApellidosEmailJefe = []
    for val in getAllDataEmpleados():
        if (val.get("codigo_jefe") == None):
            nombreApellidosEmailJefe.append(
                {
                    "puesto": val.get("puesto"),
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                    "email": val.get("email")
                    
                }
            )

    return nombreApellidosEmailJefe



def menu():
    while True:
        print("""
              

                                        ======================================

                                                REPORTES DE EMPLEADOS
                    
                                        ======================================
              




                                1. Informacion de empleados que su jefe tiene codigo 7.
            
                                2. Informacion de empleados que no son representantes de ventas.
            
                                3. Informacion del jefe de la empresa.
              
                                0. Salir
            
                        
        """)
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllNombreApellidoEmailJefeNum7(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 2):
            print(tabulate(getAllNombreApellidoPuesto(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 3):
            print(tabulate(getAllNombreApellidoEmailJefe(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 0):
            break


 





