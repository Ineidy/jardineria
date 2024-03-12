import storage.producto as produ
from tabulate import tabulate



def getAllStocksPriceGama(gama, stock): 
    condicion = []
    for val in produ.producto:
        if(val.get("gama")== gama and val.get("cantidad_en_stock") >= stock):
            condicion.append(val)

    def price(val):
        return val.get("precio_ventas")
    condicion.sort(key=price)
    for i, val in enumerate(condicion):
        if (condicion[i].get("descripcion")):
            condicion[i]["descripcion"] = f'{val.get("descripcion")[:5]}...'
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
        print("""
    ____                        __          ____          ____                 __           __            
   / __ \___  ____  ____  _____/ /____     / __ \___     / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / / / / _ \   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/  /_____/\___/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                                                             

              
                            1. obtener todos los productos de una categoria ordenando sus precios de venta, tambien de su cantidad de inventario sea superior (ejem: Ornamentales, )
                            0. Salir


""")
        

        opcion = int(input("Selecciona una opcion: "))
        if(opcion==1):
            gama = input("Seleccione la gama que desea filtrar: ")
            stock = input("ingresa la cantidad que deseas mostrar: ")
            print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 0):
            break