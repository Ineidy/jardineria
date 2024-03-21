import os
from tabulate import tabulate
import json
import requests
import module.getProductos as gP
import re


def postProducto():
        podtprodu={
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": input("Ingresa la gama: "),
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    }
    # json-server storage/producto.json -b 5007
        peticion = requests.post("http://154.38.171.54:5008/productos", data=json.dumps(podtprodu))
        res = peticion.json()
        res["Mensaje"] = "Producto Guardado"
        return [res]

def deleteproductos(id):
    peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
    if peticion.status_code == 200:
        print("produto eliminado")






def menu():
    while True:
        os.system("clear")
        print("""
              



                                        ======================================

                                            ADMINISTRAR DATOS DE PRODUCTOS
                    
                                        ======================================
              


              
                                                    
                                        1. Guardar Producto Nuevo
                                    
                                        0.salir
                
              


                
                """)
        
        opcion = int(input("Seleccione Una opcion: "))
        if(opcion>=0 and opcion<=1):
            if(opcion==1):
                print(tabulate(postProducto(), headers="keys", tablefmt='rounded_grid'))
                input("Precione una tecla para continuar......")
    
            elif(opcion==2):
                id = input("Ingrese el id de el producto que desea eliminar")
                print(deleteproductos(id))
            elif(opcion == 0):
                break
            
#s

    