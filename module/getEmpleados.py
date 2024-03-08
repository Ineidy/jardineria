

import storage.empleado as empleado
from tabulate import tabulate


def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail =[]
    for val in empleado.empleados:
        if (val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": F'{val.get("apellido1")}{val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail

def getAllNombreApellidoPuesto(codigo):
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
    print("""

   ___  _______  ____  ___  ______________  ___  ____  ______  ______  __   _______   ___  ____  ____
  / _ \/ __/ _ \/ __ \/ _ \/_  __/ __/ __/ / _ \/ __/ / __/  |/  / _ \/ /  / __/ _ | / _ \/ __ \/ __/
 / , _/ _// ___/ /_/ / , _/ / / / _/_\ \  / // / _/  / _// /|_/ / ___/ /__/ _// __ |/ // / /_/ /\ \  
/_/|_/___/_/   \____/_/|_| /_/ /___/___/ /____/___/ /___/_/  /_/_/  /____/___/_/ |_/____/\____/___/  
                                                                                                     

                            1.
                            2.
                            3.
                            4.
                            5.

    """)




 





