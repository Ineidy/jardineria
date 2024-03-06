from tabulate import tabulate

import module.getClients as cli
import module.getOficina as of
import module.getEmpleados as empleado
import module.getpago as pa
import module.getPedidos as pedi


print(tabulate(pedi.getAllCodigoEstado(), tablefmt = 'grid'))