import os
from tabulate import tabulate
import requests
import json
import module.getGama as gG

def postProduct():
    producto = {
            "codigo_producto": input("Ingrese El Codigo Del Producto: "),
            "nombre": input("Ingrese El Nombre Del Producto: "),
            "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
            "dimensiones": input("Ingrese La Dimension Del Producto: "),
            "proveedor": input("Ingrese El proveedor Del Producto: "),
            "descripcion": input("Ingrese La Descripcion Del Producto: "),
            "cantidad_en_stock": int(input("Ingrese La Cantidad Del Producto: ")),
            "precio_venta": int(input("Ingrese El Precio De Venta Del Producto: ")),
            "precio_proveedor": int(input("Ingrese El Precion De Proveedor Del Producto: "))
            }
    #headers ={'content_type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.118:5001", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "producto guardado"
    return [res]




def menu():
    while True:
        os.system("clear")
        print("""
              



                                        ======================================

                                            ADMINISTRAR DATOS DE PRODUCTOS
                    
                                        ======================================
              


              
                                                    
                                        1. Guardar Producto Nuevo}
                                    
                                        0.salir
                
              


                
                """)
        
        opcion = int(input("Seleccione Una opcion: "))
        if(opcion==1):
                print(tabulate(postProduct(), headers="Keys", tablefmt='rounded_grid'))
                input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break