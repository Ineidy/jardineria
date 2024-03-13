

import storage.empleado as empleado
from tabulate import tabulate

# empleados con jefe de codigo 7 
def getAllNombreApellidoEmailJefeNum7():
    nombreApellidoEmail =[]
    for val in empleado.empleados:
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
    for val in empleado.empleados:
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
    for val in empleado.empleados:
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

       ___  _______  ____  ___  ______________  ___  ____  ______  ______  __   _______   ___  ____  ____
      / _ \/ __/ _ \/ __ \/ _ \/_  __/ __/ __/ / _ \/ __/ / __/  |/  / _ \/ /  / __/ _ | / _ \/ __ \/ __/
     / , _/ _// ___/ /_/ / , _/ / / / _/_\ \  / // / _/  / _// /|_/ / ___/ /__/ _// __ |/ // / /_/ /\ \  
    /_/|_/___/_/   \____/_/|_| /_/ /___/___/ /____/___/ /___/_/  /_/_/  /____/___/_/ |_/____/\____/___/  
                                                                                                        

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


 





