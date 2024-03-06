from tabulate import tabulate

import module.getClients as cli
import module.getOficina as of
import module.getEmpleados as empleado 



print(tabulate(cli.getAllNombrePais('Spain'), tablefmt = 'grid'))