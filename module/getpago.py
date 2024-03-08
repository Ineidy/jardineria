import module.getpago as pa
from tabulate import tabulate

# Devuelve un listado con el codigo de cliente de aquellos clientes q realizaron algun pago en 2008. Tenga en cuenta q debera eliminar aquellos codigos de cliente q aparezcan repetidos.
def getAllCodigoClienteFecha():
    CodigoFecha = []
    codigos_vistos = set()  
    for val in pa.pago:
        if "2008" in val.get("fecha_pago"):
            Codigo_cliente = val.get("codigo_cliente")
    if ("codigo_cliente ")not in codigos_vistos:
        CodigoFecha.append(
            {
            "codigo_cliente": ("codigo_cliente"),
            "fecha": val.get("fecha_pago"),
            "total": val.get("tatal")
            }
        )
        codigos_vistos.add("codigo_cliente")
    return CodigoFecha

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

# Devuelve un listadocon todas las formas de pago q aparecen en la tabla pago. Tenga en cuenta q no deben aparecer formas de pago repetidas
def getAllFormasDePago():

    tipoPago = set()
    for val in pa.pago:
        formaPago = val.get("forma_pago")
        if formaPago not in tipoPago:
            tipoPago.add(formaPago)
    return tipoPago


def menu():
    print("""
           
   ___  _______  ____  ___  ______________  ___  ____  ___  ___  _________  ____
  / _ \/ __/ _ \/ __ \/ _ \/_  __/ __/ __/ / _ \/ __/ / _ \/ _ |/ ___/ __ \/ __/
 / , _/ _// ___/ /_/ / , _/ / / / _/_\ \  / // / _/  / ___/ __ / (_ / /_/ /\ \  
/_/|_/___/_/   \____/_/|_| /_/ /___/___/ /____/___/ /_/  /_/ |_\___/\____/___/  
                                                                                

                                                                                            

                            1. 
                            2. 
                            3. 
                            4.
                            5. 

    """)