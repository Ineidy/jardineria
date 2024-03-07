#listado de los distintos estados

import storage.pedido as pedi
from datetime import datetime


def getAllCodigoEstado():
    codigoEstado = []
    for val in pedi.pedido:
        codigoEstado.append(
            {
                "codigo": val.get ('codigo_pedido'),
                "estado": val.get ('estado')
            }
        )
    return codigoEstado


#listado de de codigo pedido, codigo cliente fecha esperadsa y 
#de entrega de pedids que no han sido entregados a tiempo


def getAllPedidosAtrasadosDeTiempo():
    PedidosAceptados = []
    for val in pedi.pedido:
        if (val.get('estado') == 'Entregado') and val.get('fecha_entrega') is None:
            val['fecha_entrega'] = val.get('fecha_esperada')
        if val.get('estado') == 'Entregado':
            date_1 = '/'.join(val.get('fecha_entrega').split('-')[::-1])
            date_2 = '/'.join(val.get('fecha_esperada').split('-')[::-1])
            start = datetime.strptime(date_1, '%d/%m/%Y')
            end = datetime.strptime(date_2, '%d/%m/%Y')
            diff = end.date() - start.datgetAllPedidosAtrasadosDeTiempoe()
            if diff.days < 0:
                PedidosAceptados.append({
                    'codigo_pedido': val.get('codigo_pedido'),
                    'codigo_cliente': val.get('codigo_cliente'),
                    'fecha_esperada': val.get('fecha_esperada'),
                    'fecha_de_entrega': val.get('fecha_entrega')

                })

    return PedidosAceptados


def getAllCodigosFechaEsoperaEntregaMenosDosDias():
    PedidosAceptados = []
    for val in pedi.pedido:
        if (val.get('estado') == 'Entregado') and val.get('fecha_entrega') is None:
            val['fecha_entrega'] = val.get('fecha_esperada')
        if val.get('estado') == 'Entregado':
            date_1 = '/'.join(val.get('fecha_esperada').split('-')[::-1])
            date_2 = '/'.join(val.get('fecha_entrega').split('-')[::-1])
            start = datetime.strptime(date_1, '%d/%m/%Y')
            end = datetime.strptime(date_2, '%d/%m/%Y')
            diff = end.date() - start.date()
            if diff.days >= 2:
                PedidosAceptados.append({
                    'codigo_pedido': val.get('codigo_pedido'),
                    'codigo_cliente': val.get('codigo_cliente'),
                    'fecha_esperada': val.get('fecha_esperada'),
                    'fecha_de_entrega': val.get('fecha_entrega')

                })

    return PedidosAceptados
    


def getAllRechazados2009():
    rechazados2009 = []
    for val in pedi.pedido:
        if (val.get('estado') == 'Rechazado') and  val.get('estado').startswith("2009"):
            rechazados2009.append({
                'codigo_pedido': val.get('codigo_pedido'),
                'estado': val.get('Estado')
            })
            
            