from tabulate import tabulate

import module.getClients as cliente 

print(tabulate(cliente.getAllClientPaisRegionCiudad('Spain', 'Fuenlabrada', 'Madrid'), tablefmt = 'grid'))