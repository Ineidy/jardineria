#listado de los distintos estados
from datetime import datetime
from tabulate import tabulate
import requests

def getAllDataPedidos():
     # json-server storage/pedido.json -b 5006
    peticionpedidos= requests.get("http://154.38.171.54:5007/pedidos")
    datapedidos = peticionpedidos.json()
    return datapedidos



#ver el codigo de cada pedido y su estado
def getAllCodigoEstado():
    codigoEstado = []
    for val in getAllDataPedidos():
        codigoEstado.append(
            {
                "codigo": val.get ("codigo_pedido"),
                "estado": val.get ("estado")
            }
        )
    return codigoEstado


#listado de de codigo pedido, codigo cliente fecha esperada y 
#de entrega de pedidos que no han sido entregados a tiempo



def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for pedidos in getAllDataPedidos():
        if (pedidos.get("estado") == "Entregado" and pedidos.get("fechaEntrega") is None):
            pedidos["fechaEntrega"]= pedidos.get("fecha_esperada")
            
        if pedidos.get("estado") == "Entregado":

            date_1 = "/".join(pedidos.get("fechaEntrega").split("-")[::-1])
            date_2 = "/".join(pedidos.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0 :
                pedidosEntregado.append({
                    "codigo_pedido": pedidos.get("codigo_pedido"),
                    "codigo_cliente": pedidos.get("codigo_cliente"),
                    "fecha_esperada": pedidos.get("fecha_esperada"),
                    "fecha_de_entrega": pedidos.get("fechaEntrega")
                })

    return pedidosEntregado

#Pedidos con fecha de espera de menos de dos dias
def getAllPedAntesFechaEsperada():
    pedidosAntesFechaEsperada = []
    for val in getAllDataPedidos():

        if (val.get("estado") == "Entregado" and val.get("fechaEntrega") is None):
            val["fechaEntrega"]= val.get("fecha_esperada")
            
        if(val.get("estado") == "Entregado"):

            date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days >= 2 :
                pedidosAntesFechaEsperada.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fechaEntrega")
                })

    return pedidosAntesFechaEsperada

#pedidos rechazados en 2009
def getAllPedRechazadosEn2008():
    pedidosRechazadosEn2008 = []
    for val in getAllDataPedidos():
        if val.get("estado") == "Rechazado":
            if val.get("fecha_pedido")[0:4] == "2008" and val.get("fecha_esperada")[0:4] == "2008":
                pedidosRechazadosEn2008.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "estado": val.get("estado"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })

    return pedidosRechazadosEn2008


# Devuelve un listado de todos los pedidos q han sido entregados en el mes de enero de cualquier año

def getAllPedEntEnero():
    AllPedEntEnero = []
    for val in getAllDataPedidos():

        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") is None):
            val["fecha_entrega"]= val.get("fecha_esperada")

        if val.get("estado") == "Entregado":

            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
        
             
            if start.month == 1  :
                AllPedEntEnero.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })

    return AllPedEntEnero



def menu():
    while True:
        print("""

                                        ======================================

                                                REPORTES DE PEDIDOS
                    
                                        ======================================
              



                                                                                            
                                
                                1. Codigo y estado de cada pedido.
            
                                2. Informacion de pedidos que no han sido entregados a tiempo.
            
                                3. Pedidos con fecha de espera de menos de dos dias.
            
                                4. Pedidos rechazados en 2008.
            
                                5. Pedidos entregados en enero de cualquier año.
              
                                0. Salir
            



    """)
        
        opcion = int(input("Selecciones una opcion: "))
        if (opcion == 1):
            print(tabulate(getAllCodigoEstado(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 2):
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 3):
            print(tabulate(getAllPedAntesFechaEsperada(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 4):
            print(tabulate(getAllPedRechazadosEn2008(),headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 5):
            print(tabulate(getAllPedEntEnero(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break



        #mal 2 y 3