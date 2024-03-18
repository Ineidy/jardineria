import requests
from tabulate import tabulate
import module.getClients as reportesclientes
import module.getEmpleados as reportesempleados


def getAllDataPago():
     # json-server storage/pago.json -b 5005
    peticionpago= requests.get("http://192.168.10.159:5005")
    datapago = peticionpago.json()
    return datapago


#Devuelve un listado con el codigo de cliente de aquellos 
#clientes q realizaron algun pago en 2008. 
#Tenga en cuenta q debera eliminar aquellos codigos de cliente q 
#aparezcan repetidos.


def getAllCodigoClienteFecha():
    codigos_vistos = {}
    for val in getAllDataPago():
        if( "2008" in val.get("fecha_pago") and "codigo_cliente ")not in ("codigos_vistos"):
            codigos_vistos.append(
                {
                'codigo_cliente': val.get('codigo_cliente'),
                'fecha': val.get('fecha_pago'),
                'total': val.get('tatal')
                }
            )
            codigos_vistos.add("codigo_cliente")
    return codigos_vistos

#Devuelve un listado con todos los pagos q se realizaron en en el año 2008 mediante paypal, ordena el resultado de mayor a menor
def getAllPagosFecha():
    pagosFecha = []
    for val in getAllDataPago():
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") is ("PayPal"):
            pagosFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"])
    return pagosFecha

# Devuelve un listado con todas las formas de pago q aparecen en la tabla pago. Tenga en cuenta q no deben aparecer formas de pago repetidas

def getAllFormasDePago():
    formasDePago = set()
    detallesDePago = []
    for val in getAllDataPago():
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
    for val in getAllDataPago():
        for i in reportesclientes:
            for u in reportesempleados:
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
    for val in getAllDataPago():
        for i in cli.cliente:
            for u in reportesempleados:
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
        if(opcion == 1):
            print(tabulate(getAllCodigoClienteFecha(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 2):
            print(tabulate(getAllPagosFecha(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 3):
            print(tabulate(getAllFormasDePago(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            print(tabulate(getAllClientsPagosConReprVentas(),headers="keys",tablefmt='rounded_grid'))
        elif(opcion == 5):
            print(tabulate(getAllNoPagosReprVentas(),headers="keys",tablefmt='rounded_grid'))
        elif(opcion == 0):
            break



        #mal 1, 5