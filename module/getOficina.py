import requests
from tabulate import tabulate
import os


def getAllDataoficina():
     # json-server storage/oficina.json -b 5004
    peticionofi= requests.get("http://192.168.10.159:5004")
    dataofi = peticionofi.json()
    return dataofi


#filto para mirar el codigo y ciudad de las oficinas
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllDataoficina():
        codigoCiudad.append({
        "codigo": val.get("codigo_oficina"),
        "ciudad": val.get("ciudad")
        })

    return codigoCiudad

#ciudad y telefono de las oficias de españa
def getAllCiudadTelefono():
    ciudadTelefono =[]
    for val in getAllDataoficina():
        if (val.get("pais") == 'España'):
            ciudadTelefono.append({
                "pais": val.get("pais"),
                "ciudad": val.get("ciudad"),
                "telefono":val.get("telefono"),

            })
    return ciudadTelefono


def getAllInfoPais(pais):
    infoPais =[]
    for val in getAllDataoficina():
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
        os.system("clear")
        print("""
    
                                        ====================================

                                                REPORTES DE OFICINAS
                    
                                        ====================================





                                                                                                

                                
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
        
        
#D