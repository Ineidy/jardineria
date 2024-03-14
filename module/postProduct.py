import json
import requests
import os
from tabulate import tabulate
import module.getGama as gG

def postProduct():
    producto = {
            "codigo_producto": input("Ingrese El Codigo Del Producto: "),
            "nombre": input("Ingrese El Nombre Del Producto: "),
            "gama": input("Ingrese La Gama Del Producto: "),
            "dimensiones": input("Ingrese La Dimension Del Producto: "),
            "proveedor": input("Ingrese El proveedor Del Producto: "),
            "descripcion": input("Ingrese La Descripcion Del Producto: "),
            "cantidad_en_stock": int(input("Ingrese La Cantidad Del Producto: ")),
            "precio_venta": int(input("Ingrese El Precio De Venta Del Producto: ")),
            "precio_proveedor": int(input("Ingrese El Precion De Proveedor Del Producto: "))
            }
    headers ={'content_type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.118:5001", data=json.dumps(producto))

    res = peticion.json
    res["Mensaje"] = "producto guardado"
    return [res]




def menu():
    while True:
        os.system("clear")
        print("""

             ______    ___      _                   
            / ____/___/ (_)____(_)___  ____         
           / __/ / __  / / ___/ / __ \/ __ \        
          / /___/ /_/ / / /__/ / /_/ / / / /        
         /_____/\__,_/_/\___/_/\____/_/ /_/         
                      / __ \___                     
                     / / / / _ \                    
                    / /_/ /  __/                    
    ____           /_____/\___/       __            
   / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                    
                1. Guardar Producto Nuevo
                0.salir
                
                
                """)
        
        opcion = int(input("Seleccione Una opcion: "))
        if(opcion==1):
                print(tabulate(postProduct(), headers="Keys", tablefmt='rounded_grid'))
                input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break