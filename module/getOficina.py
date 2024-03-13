import storage.oficina as of
from tabulate import tabulate

#filto para mirar el codigo y ciudad de las oficinas
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
        "codigo": val.get("codigo_oficina"),
        "ciudad": val.get("ciudad")
        })

    return codigoCiudad

#ciudad y telefono de las oficias de españa
def getAllCiudadTelefono():
    ciudadTelefono =[]
    for val in of.oficina:
        if (val.get("pais") == 'España'):
            ciudadTelefono.append({
                "pais": val.get("pais"),
                "ciudad": val.get("ciudad"),
                "telefono":val.get("telefono"),

            })
    return ciudadTelefono


def getAllInfoPais(pais):
    infoPais =[]
    for val in of.oficina:
        if (val.get("pais") == pais):
            infoPais.append({
                "pais": val.get("pais"),
                "codigo_oficina": val.get("codigo_oficina"),
                "codigo_postal": val.get("codigo_postal"),
                "ciudad": val.get("ciudad"),
                "telefono":val.get("telefono")

            })
    return infoPais
                

def menu():
    while True:

        print("""
    
       ___  _______  ____  ___  ______________  ___  ____  ____  __________________  _____   ____
      / _ \/ __/ _ \/ __ \/ _ \/_  __/ __/ __/ / _ \/ __/ / __ \/ __/  _/ ___/  _/ |/ / _ | / __/
     / , _/ _// ___/ /_/ / , _/ / / / _/_\ \  / // / _/  / /_/ / _/_/ // /___/ //    / __ |_\ \  
    /_/|_/___/_/   \____/_/|_| /_/ /___/___/ /____/___/  \____/_/ /___/\___/___/_/|_/_/ |_/___/  
                                                                                                

                                
                                1. Obtener los codigos de oficina y ciudad.
            
                                2. Obtener oficinas de España.
            
                                3. Obtener oficinas de cualquier pais.
              
                                0. Salir


        """)
        opcion = int(input("Seleccione una opcion: "))
        if(opcion == 1):
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt= 'rounded_grid'))
        elif(opcion == 2):
            print(tabulate(getAllCiudadTelefono(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 3):
            pais = input("Ingrese de que pais quiere buscar la oficina: ")
            print(tabulate(getAllInfoPais(pais), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 0):
            break