import storage.pago as pa
import storage.cliente as cli
import storage.empleado as empleado
from tabulate import tabulate

#Devuelve un listado con el codigo de cliente de aquellos 
#clientes q realizaron algun pago en 2008. 
#Tenga en cuenta q debera eliminar aquellos codigos de cliente q 
#aparezcan repetidos.


# def getAllCodigoClienteFecha():
#     codigos_vistos = {}
#     for val in pa.pago:
#         if "2008" in val.get("fecha_pago"):
#             Codigo_cliente = val.get("codigo_cliente")
#     if ("codigo_cliente ")not in codigos_vistos:
#         codigos_vistos.append(
#             {
#             'codigo_cliente': val.get('codigo_cliente'),
#             'fecha': val.get('fecha_pago'),
#             'total': val.get('tatal')
#             }
#         )
#         codigos_vistos.add("codigo_cliente")
#     return codigos_vistos

# Devuelve un listado con todos los pagos q se realizaron en en el año 2008 mediante paypal, ordena el resultado de mayor a menor
# def getAllPagosFecha():
#     pagosFecha = []
#     for val in pa.pago:
#         if("2008") in val.get("fecha_pago") and val.get("forma_pago") is ("PayPal"):
#             pagosFecha.append({
#                     "codigo_de_cliente": val.get("codigo_cliente"),
#                     "fecha_pago": val.get("fecha_pago"),
#                     "forma_pago": val.get("forma_pago"),
#                     "total": val.get("total")
#                 })
#     pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"])
#     return pagosFecha

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

#Muestre el nombre de los clientes que hayan realizado pagos y el nombre de su representante de ventas

def getAllClientsPagosConReprVentas():
    clientsPagosConReprventas = []
    for val in pa.pago:
        for i in cli.clientes:
            for u in empleado.empleados:
                if(
                    i.get("codigo_cliente") == val.get("codigo_cliente")  and
                    i.get("codigo_empleado_rep_ventas") == u.get("codigo_empleado")
                ):
                    clientsPagosConReprventas.append(
                            {
                                "Codigo_Del_Cliente": i.get ('codigo_cliente'),
                                "Nombre": i.get ('nombre_cliente'),
                                "Representante_Ventas": u.get('nombre')

                            }
                        )
                
    return clientsPagosConReprventas

#Muestre el nombre de los clientes que NO hayan realizado pagos y el nombre de su representante de ventas
def getAllNoPagosReprVentas():
    noPagosRepVentas=[]
    for val in pa.pago:
        for i in cli.clientes:
            for u in empleado.empleados:
                if(
                    i.get("codigo_cliente") is not val.get("codigo_cliente") and
                    i.get("codigo_empleado_rep_ventas") == u.get("codigo_empleado")
                ):
                    noPagosRepVentas.append(
                        {
                            "Codigo_Del_Cliente": i.get ('codigo_cliente'),
                            "Nombre": i.get ('nombre_cliente'),
                            "Representante_Ventas": u.get('nombre')
                        }
                    )

    return noPagosRepVentas

def menu():
    while True:
        print("""
            
                                        ======================================

                                                  REPORTES DE PAGOS
                    
                                        ======================================
              

              
                                                                                    

                                                                                                

                                1. Codigo de clientes que realizaron pagos en 2008, sin repetir.
            
                                2. Pagos realizados en 2008 por PayPal, de mayor a menor. 
            
                                3. Todas las formas de pago sin repetir.
            
                                4. Nombre de los clientes que hayan realizado pagos y sus representantes de ventas.
            
                                5. Nombre de los clientes que NO hayan realizado pagos y sus representantes de ventas.
                                
                                0. Salir
                                
        """)
        
        opcion = int(input("Seleccione una opcion: "))
        # if(opcion == 1):
        #     print(tabulate(getAllCodigoClienteFecha(), headers="keys", tablefmt='rounded_grid'))
        # elif(opcion == 2):
        #     print(tabulate(getAllPagosFecha(), headers="keys", tablefmt='rounded_grid'))
        if(opcion == 3):
            print(tabulate(getAllFormasDePago(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            print(tabulate(getAllClientsPagosConReprVentas(),headers="keys",tablefmt='rounded_grid'))
        elif(opcion == 5):
            print(tabulate(getAllNoPagosReprVentas(),headers="keys",tablefmt='rounded_grid'))
        elif(opcion == 0):
            break



        #corregir 1 