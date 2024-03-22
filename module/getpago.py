import requests
from tabulate import tabulate
from datetime import datetime
import module.postpagos as postpag
import module.postEmpleados as postemp
import module.postClientes as postcli
import module.getClients as reportesclientes
import module.getEmpleados as reportesempleados


#Devuelve un listado con el codigo de cliente de aquellos 
#clientes q realizaron algun pago en 2008. 
#Tenga en cuenta q debera eliminar aquellos codigos de cliente q 
#aparezcan repetidos.


def getCodClientesPago2008():
    codigosclientespago2008 = []
    for val in postpag.getAllDataPago():
        año = val.get("fecha_pago")

        if año.startswith("2008"):  
            codigosclientespago2008.append(
                {
                    "fecha_pago": val.get("fecha_pago"),
                    "codigo_cliente": val.get("codigo_cliente")
                }
            )

    codigosclientespago2008 = list(set(tuple(item.items()) for item in codigosclientespago2008))

    return codigosclientespago2008

#Devuelve un listado con todos los pagos q se realizaron en en el año 2008 mediante paypal, ordena el resultado de mayor a menor


def getAllPagPayPal():
    AllPagPayPal = []
    for val in postpag.getAllDataPago():

        pago= "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(pago, "%d/%m/%Y")

        if(val.get("forma_pago") == "PayPal" and start.year == 2008):
            AllPagPayPal.append({
                "forma_pago" :(val.get("forma_pago")),
                "fecha_pago" :(val.get("fecha_pago")),
                "total": (val.get("total"))
            })

    AllPagPayPal = sorted(AllPagPayPal, key=lambda x: x["total"], reverse=True)

    return AllPagPayPal


# Devuelve un listado con todas las formas de pago q aparecen en la tabla pago. Tenga en cuenta q no deben aparecer formas de pago repetidas


def getAllFormasPago():
    FormasPago = list()
    for FP in postpag.getAllDataPago():
        if(FP.get("forma_pago") != None):
            FormasPago.append({
                "forma_pago" : (FP.get("forma_pago"))
            })

    FormasPago = list(set(tuple(item.items()) for item in FormasPago))
    
    return FormasPago

#Muestre el nombre de los clientes que hayan realizado pagos y el nombre de su representante de ventas
def getAllClientPag():
    allClientPag =[]
    for val in postpag.getAllDataPago():
        for val2 in postcli.getAllDataClientes():
            for val3 in postemp.getAllDataEmpleados():
                if val2.get("codigo_cliente") == val.get("codigo_cliente") and val2.get("codigo_empleado_rep_ventas") == val3.get("codigo_empleado"): 

                    allClientPag.append(
                        {
                            "codigo_cliente":val.get("codigo_cliente"),
                            "nombre":val2.get("nombre_cliente"),
                            "cod_representante": val2.get("codigo_empleado_rep_ventas"),
                            "nombre_empleado": val3.get("nombre")
                        }
                    )
    return allClientPag

#Muestre el nombre de los clientes que NO hayan realizado pagos y el nombre de su representante de ventas
def getAllNoPay():
    allNoPay = []
    for val in postcli.getAllDataClientes():
        pagos = False
        for d in postpag.getAllDataPago():
                if val.get('codigo_cliente')== d.get('codigo_cliente'):
                    pagos = True
                    break
        if not pagos:
            for d in postemp.getAllDataEmpleados():
                if val.get('codigo_empleado_rep_ventas') == d.get('codigo_empleado'):
                    if d.get('puesto') == 'Representante Ventas':
                        allNoPay.append({

                                'codigo': val.get('codigo_cliente'),
                                "Nombre Cliente": val.get("nombre_cliente"),
                                "puesto": d.get("puesto"),
                                "Representante de ventas": d.get('nombre')
                            })
    return allNoPay

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
            print(tabulate(getCodClientesPago2008(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 2):
            print(tabulate(getAllPagPayPal(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion == 3):
            print(tabulate(getAllFormasPago(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            print(tabulate(getAllClientPag(),headers="keys",tablefmt='rounded_grid'))
        elif(opcion == 5):
            print(tabulate(getAllNoPay(),headers="keys",tablefmt='rounded_grid'))
        elif(opcion == 0):
            break



        #mal 1, 5