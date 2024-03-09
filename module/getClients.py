import storage.cliente as cli
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



def menu():
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


""")
    
    opcion = int(input("\nElija una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllClientesName(), headers="keys", tablefmt = 'rounded_grid'))
    
    elif(opcion == 2):
        codigoCliente = int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getOneClientCodigo(codigoCliente), headers="keys",tablefmt = 'rounded_grid'))
    
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