import module.getpago as pa
from tabulate import tabulate

#Devuelve un listado con el codigo de cliente de aquellos 
#clientes q realizaron algun pago en 2008. 
#Tenga en cuenta q debera eliminar aquellos codigos de cliente q 
#aparezcan repetidos.


def getAllCodigoClienteFecha():
    codigos_vistos = {}
    for val in pa.pago:
        if "2008" in val.get("fecha_pago"):
            Codigo_cliente = val.get("codigo_cliente")
    if ("codigo_cliente ")not in codigos_vistos:
        codigos_vistos.append(
            {
            "codigo_cliente": ("codigo_cliente"),
            "fecha": val.get("fecha_pago"),
            "total": val.get("tatal")
            }
        )
        codigos_vistos.add("codigo_cliente")
    return codigos_vistos

# Devuelve un listado con todos los pagos q se realizaron en en el año 2008 mediante paypal, ordena el resultado de mayor a menor
def getAllPagosFecha():
    pagosFecha = []
    for val in pa.pago:
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") is ("PayPal"):
            pagosFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"], reverse=True)
    return pagosFecha

# Devuelve un listado con todas las formas de pago q aparecen en la tabla pago. Tenga en cuenta q no deben aparecer formas de pago repetidas

def getAllFormasDePago():
    formasDePago = set()
    detallesDePago = []
    for val in pa.pago:
        formaPago = val.get("forma_pago")
        if formaPago not in formasDePago:
            formasDePago.add(formaPago)
            detallesDePago.append({
                "pago": val.get('forma_pago')
            })

    return detallesDePago

def menu():
    print("""
           
   ___  _______  ____  ___  ______________  ___  ____  ___  ___  _________  ____
  / _ \/ __/ _ \/ __ \/ _ \/_  __/ __/ __/ / _ \/ __/ / _ \/ _ |/ ___/ __ \/ __/
 / , _/ _// ___/ /_/ / , _/ / / / _/_\ \  / // / _/  / ___/ __ / (_ / /_/ /\ \  
/_/|_/___/_/   \____/_/|_| /_/ /___/___/ /____/___/ /_/  /_/ |_\___/\____/___/  
                                                                                

                                                                                            

                            1. Codigo de clientes que realizaron pagos en 2008, sin repetir.
          
                            2. Pagos realizados en 2008 por PayPal, de mayor a menor. 
          
                            3. Todas las formas de pago sin repetir.
                            
    """)
     
    opcion = int(input("Seleccione una opcion: "))
    if(opcion == 1):
        print(tabulate(getAllCodigoClienteFecha(), headers="keys", tablefmt='rounded_grid'))
    elif(opcion == 2):
        print(tabulate(getAllPagosFecha(), headers="keys", tablefmt='rounded_grid'))
    elif(opcion == 3):
        print(tabulate(getAllFormasDePago(), headers="keys", tablefmt='rounded_grid'))


    #corregir los 3 :/