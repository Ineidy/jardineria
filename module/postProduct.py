import os
from tabulate import tabulate
import json
import requests


def postProducto():
    # json-server storage/producto.json -b 5007
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": input("Ingresa la gama: "),
        #gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    }
    
    peticion = requests.post("http://192.168.10.159:5007", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



# def postProduct():
#     producto = dict()
#     while True:
#         try:
#             #expresion regular que valide de una cadena de numeros y letras en mayusculas, cumple con los estandares
#             if(not producto.get("codigo_producto")):
#                 codigo = input("Ingrese el codigo del producto: ")
#                 if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
#                     data = gP.getProductCodigo(codigo)
#                     if(data):
#                         print(tabulate(data, headers="keys", tablefmt='rounded_grid'))
#                         raise Exception("El codigo del proyucto ya existe")
#                     else: 
#                         producto["codigo_producto"] = codigo
#                 else: 
#                     raise Exception("El codigo del producto no cumple con los estandares establecidos")
                
#             #Expresion regular que valida de una cadena solo letrar pero las primeros letras en mayuscula
#             if(not producto.get("nombre")):
#                 nombre = input("Ingrese el nombre del producto: ")
#                 if(re.match(r'^([A-Z][a-z]*\s*)+$', nombre)is not None):
#                     producto["nombre"] = nombre
#                     break 
#                 else:
#                     raise Exception("El nombre del producto no cumple con el estandar establecido")
                
#         except Exception as error:
#             print(error)


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
        # if(re.match(r'^[0-9]+$', opcion)is not None):
        #     opcion =int(opcion)
        #     if(opcion>=0 and opcion<=1):
        #         if(opcion==1):
        #             print(tabulate(postProduct(), headers="keys", tablefmt='rounded_grid'))
        #             input("Precione una tecla para continuar......")
       
       
        if(opcion==1):
                print(tabulate(postProducto(), headers="Keys", tablefmt='rounded_grid'))
                input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
        
#s