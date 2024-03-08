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
    for val in cli.clientes:
        if (val.get('codigo_cliente') == codigo):
            return{
               "codigo_cliente": val.get('codigo_cliente'),
               "nombre_cliente": val.get('nombre_cliente') 
            }
    
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = []
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(val)
    return clienteCredic

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = []
    for val in cli.clientes:
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) and
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone


def getAllNombrePais(pais):
    nombrePais = []
    for val in cli.clientes:
        if (val.get("pais") == pais):
            nombrePais.append(
                {
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
                                                                                            

          1. obtener todos los clientes (nombre)
          2. obtener un cliente por el codigo (codigo y nombre)
          3. obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000, San Francisco)

    """)
opcion = int(input("\nSeleccione una de las opciones: "))
if(opcion == 1):
    print(tabulate(getAllClientesName)(), headers="keys", tablefmt = 'rounded_grid')
elif(opcion == 2):
    codigoCliente = int(input("Ingrese el codigo del cliente: "))
    print(tabulate(getOneClientCodigo)(codigoCliente), headers="keys",tablefmt = 'rounded_grid')

