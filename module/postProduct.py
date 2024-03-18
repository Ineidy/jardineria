import os
from tabulate import tabulate
import json
import requests
import module.getProductos as gP
import re


def postProducto():
    # json-server storage/producto.json -b 5007
        # peticion = requests.post("http://192.168.10.159:5007", data=json.dumps(producto))
        # res = peticion.json()
        # res["Mensaje"] = "Producto Guardado"
        # return [res]



producto = dict()

while True:
         
    try: 
        if(not producto.get("codigo_producto")):    
            codigo = input("Ingresa el codigo del producto: ")
            if (re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                    producto["codigo_producto"] = codigo

            else: 
                raise Exception("El codigo del producto no cumple con los estandares establecidos")

        nombre = input("Ingresa el nombre del producto: ")
        if(re.match(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$', nombre)is not None):
            nombre["nombre"] = nombre
                    
        else: 
            raise Exception("El nombre del producto no cumple con los estandares establecidos")


    except Exception as error:
         print("ERROR")
         print(error)








def deleteProducto(id):
    data = gP.getProductoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://192.168.10.159:5007/productos/{id}")
        if(peticion.status_code == 204):
             data.append({"Mensaje": "Producto eliminado correctamente"})
             return {
                  "body": data,
                  "status": peticion.status_code,
             }
    else:
         return{
              "body":[{
                   "Mensaje":"producto no encontrado"
              }]
         }

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
        if(re.match(r'[0-9]+$' , opcion)is not None):
            opcion =int(opcion)
            if(opcion>=0 and opcion<=1):
                if(opcion==1):
                    print(tabulate(postProduct(), headers="keys", tablefmt='rounded_grid'))
                    input("Precione una tecla para continuar......")
       
       
        if(opcion==1):
                print(tabulate(postProducto(), headers="Keys", tablefmt='rounded_grid'))
                input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
        
#s
    #     "codigo_producto": input("Ingrese el codigo del producto: "),
    #     "nombre": input("Ingrese el nombre del producto: "),
    #     "gama": input("Ingresa la gama: "),gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
    #     "dimensiones": input("Ingrse la dimensiones del producto: "),
    #     "proveedor": input("Ingrse el proveedor del producto: "),
    #     "descripcion": input("Ingrse el descripcion del producto: "),
    #     "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
    #     "precio_venta": int(input("Ingrse el precio de ventas: ")),
    #     "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    # }
    