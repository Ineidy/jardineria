import storage.cliente as cli
import storage.empleado as empleado
from tabulate import tabulate

def getAllClientesName():
    clienteName = []
    for val in cli.clientes:
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    clienteCodigo = []
    for val in cli.clientes:
        if (val.get('codigo_cliente') == codigo):
            clienteCodigo.append({
               "codigo": val.get('codigo_cliente'),
               "nombre": val.get('nombre_cliente') 
            })
    return clienteCodigo
    
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = []
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append({
                "codigo": val.get('codigo_cliente'),
                "nombre": val.get('nombre_cliente'),
                "limite_credicticio": val.get('limite_credito'),
                "Pais": val.get('pais'),
                "Ciudad": val.get('ciudad')
            })
    return clienteCredic

def getAllClientPaisRegionCiudad(pais, region, ciudad):
    clientZone = []
    for val in cli.clientes:
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) and
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append({
                "codigo": val.get('codigo_cliente'),
                "nombre": val.get('nombre_cliente'),
                "Region": val.get('region'),
                "Pais": val.get('pais'),
                "Ciudad": val.get('ciudad')
            })
    return clientZone


def getAllNombrePais(pais):
    nombrePais = []
    for val in cli.clientes:
        if (val.get("pais") == pais):
            nombrePais.append(
                {
                "codigo": val.get('codigo_cliente'),
                "nombre":val.get('nombre_cliente'),
                "pais": val.get('pais')
                }
            )

    return nombrePais


#devuelve un listado con todos los clientes que sean de la ciudad de Madrid 
#y cuyo representante de ventas tenga el codigo de empleado 11 o 30.
def getAllClientsMadridRepVentas30o11():
    clientsMadrid = []
    for val in cli.clientes:
        if( 
            val.get('ciudad') == 'Madrid' and 
            (val.get('codigo_empleado_rep_ventas') == 11 or val.get('codigo_empleado_rep_ventas') == 30)

        ):
            clientsMadrid.append(
                {
                    "Codigo_Del_Cliente": val.get('codigo_cliente'),
                    "Nombre_Del_Cliente": val.get('nombre_cliente'),
                    "Codigo_De_Empleado": val.get('codigo_empleado_rep_ventas'),
                    "Ciudad": val.get('ciudad')
                }
            )
    return clientsMadrid




#obtener un listado con el nombre de cada cliente y el nombre y apellido del representante de ventas
def getAllClientesReprVentas():
    clientsReprVentas = []
    for val in cli.clientes:
        for i in empleado.empleado:
            if val.get("codigo_empleado_rep_ventas") == i.get("codigo_empleado"):
                clientsReprVentas.append(
                    {
                     "Nombre":val.get('nombre_cliente'),
                     "Apellidos": F'{val.get("apellido1")}{val.get("apellido2")}'
                    }
                )
        return clientsReprVentas

        
        



def menu():
    while True:
        print("""
            

       ___  _______  ____  ___  ______________  ___  ____  _______   _________  ________________
      / _ \/ __/ _ \/ __ \/ _ \/_  __/ __/ __/ / _ \/ __/ / ___/ /  /  _/ __/ |/ /_  __/ __/ __/
     / , _/ _// ___/ /_/ / , _/ / / / _/_\ \  / // / _/  / /__/ /___/ // _//    / / / / _/_\ \  
    /_/|_/___/_/   \____/_/|_| /_/ /___/___/ /____/___/  \___/____/___/___/_/|_/ /_/ /___/___/  
                                                                                                

            1. obtener todos los clientes (nombre).

            2. obtener un cliente por el codigo.

            3. obtener toda la informacion de un cliente segun su limite de credito
                y ciudad que pertenece (ejem: 3000, San Francisco).
            
            4. obtener clientes por pais, region y ciudad.

            5. obtener cliente por pais.

            6. obtener listado con todos los clientes que sean de la ciudad de Madrid y cuyo representante de ventas tenga el codigo de empleado 11 o 30.
              
            7. obtener cada cielte con su representante de ventas
              
            0. Salir


    """)
        
        opcion = int(input("\nElija una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllClientesName(), headers="keys", tablefmt = 'rounded_grid'))
        
        elif(opcion == 2):
            codigo = int(input("Ingrese el codigo del cliente: "))
            print(tabulate(getOneClientCodigo(codigo), headers="keys",tablefmt = 'rounded_grid'))
        
        elif(opcion == 3):
            limite = int(input("Ingrese el limite de credito de los clientes que deseas visualizar: "))
            ciudad = input("ingrese la ciudad que desea filtrar los clientes: ")
            print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers="keys", tablefmt='rounded_grid'))
        
        elif(opcion == 4):
            pais = input("Ingrese el pais que desea filtrar: ")
            region = input("Ingrese la region que desea filtrar: ")
            ciudad = input("Ingrese la ciudad que desea filtrar: ")
            print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt='rounded_grid'))

        elif(opcion == 5):
            pais = input("Ingrese el pais del que quiere filtrar el cliente: ")
            print(tabulate(getAllNombrePais(pais), headers="keys", tablefmt="rounded_grid"))

        elif(opcion==6):
            print(tabulate(getAllClientsMadridRepVentas30o11(), headers="keys", tablefmt='rounded_grid'))

        elif(opcion==7):
            print(tabulate(getAllClientesReprVentas(),headers="keys", tablefmt='rounded_grid'))

        elif(opcion==0):
            break