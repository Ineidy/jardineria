from tabulate import tabulate
import os
import requests

# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales 
# y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, 
# mostrando en primer lugar los de mayor precio.
def getAllData():
     # json-server storage/producto.json -b 5501
    peticion= requests.get("http://172.16.100.118:5001")
    data = peticion.json()
    return data

def getAllStocksPriceGama(gama, stock): 
    condicion = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condicion.append(val)

    def price(val):
        return val.get("precio_ventas")
    condicion.sort(key=price, reverse=True)
    for i, val in enumerate(condicion):
        condicion[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condicion[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")
            }
    return condicion

def menu():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                                REPORTES DE PRODUCTOS
                    
                                        ======================================    
              





              
                            1. obtener todos los productos de una categoria ordenando sus precios de venta, tambien de su cantidad de inventario 
                            sea superior (ejem: Ornamentales, )
        
                            0. Salir

        """)
        

        opcion = int(input("Selecciona una opcion: "))
        if(opcion==1):
            gama = input("Ingrese la gama que deseas flictrar: ")
            stock = int(input("Ingrese las unidades que seas mostrar: "))
            print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="github"))
        elif(opcion == 0):
            break