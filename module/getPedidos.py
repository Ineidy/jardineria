#listado de los distintos estados

import storage.pedido as pedi
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