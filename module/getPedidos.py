#listado de los distintos estados
from datetime import datetime
from tabulate import tabulate
import requests

def getAllDataPedidos():
     # json-server storage/pedido.json -b 5006
    peticionpedidos= requests.get("http://192.168.10.159:5006")
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
    for val in getAllDataPedidos():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end =   datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                pedidosEntregado.append({
                    "código_de_pedido": val.get("codigo_pedido"),
                    "código_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                })
    return pedidosEntregado

#Pedidos con fecha de espera de menos de dos dias
def getAllCodigosFechaEsperaEntregaMenosDosDias():
    PedidosAceptados = []
    for val in getAllDataPedidos():
        if (val.get("estado") == "Entregado") and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1]) 
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end =   datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days >= 2:
                PedidosAceptados.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")

                })

    return PedidosAceptados
    
#pedidos rechazados en 2009

def getAllPedidosRechazados():
    pedidosRechazados = []
    for val in getAllDataPedidos():
        if("2009") in val.get("fecha_pedido") and val.get("estado") is ("Rechazado"):
            pedidosRechazados.append({

                    "codigo_pedido": val.get("codigo_pedido"),
                    "Fecha De Rechazo": val.get("fecha_pedido"),
                    "estado_pedido": val.get("estado")
                })
    return pedidosRechazados
            

# Devuelve un listado de todos los pedidos q han sido entregados en el mes de enero de cualquier año
def getAllPedidosEntregadosEnero():
    pedidosEntregadosMes = []
    for val in getAllDataPedidos():
        fecha_entrega = val.get("fecha_entrega")
        if fecha_entrega:
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            if start.month == 1 and val.get("estado") == "Entregado":
                pedidosEntregadosMes.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                    "estado_pedido": val.get("estado")
                })
    return pedidosEntregadosMes


def menu():
    while True:
        print("""

                                        ======================================

                                                REPORTES DE PEDIDOS
                    
                                        ======================================
              



                                                                                            
                                
                                1. Codigo y estado de cada pedido.
            
                                2. Informacion de pedidos que no han sido entregados a tiempo.
            
                                3. Pedidos con fecha de espera de menos de dos dias.
            
                                4. Pedidos rechazados en 2009.
            
                                5. Pedidos entregados en enero de cualquier año.
              
                                0. Salir
            



    """)
        
        opcion = int(input("Selecciones una opcion: "))
        if (opcion == 1):
            print(tabulate(getAllCodigoEstado(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 2):
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 3):
            print(tabulate(getAllCodigosFechaEsperaEntregaMenosDosDias(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 4):
            print(tabulate(getAllPedidosRechazados(),headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 5):
            print(tabulate(getAllPedidosEntregadosEnero(), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break



        #mal 2 y 3