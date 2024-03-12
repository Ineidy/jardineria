from tabulate import tabulate

import module.getProductos as produ
import module.getClients as cli
import module.getOficina as of
import module.getEmpleados as empleado
import module.getpago as pa
import module.getPedidos as pedi

if (__name__ == '__main__'):
    while True:
        print("""
        __  ___                    ____       _            _             __
       /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
      / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
     / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
    /_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                        /_/               


                                1. cliente
                                2. oficina
                                3. empleados
                                4. pedidos 
                                5. pagos
                                6. productos
                                0. salir
    """)
        
        opcion = int(input("\n Seleccione una de las opciones: "))
        if(opcion == 1):
            cli.menu()
        elif(opcion == 2):
            of.menu()
        elif(opcion == 3):
            empleado.menu()
        elif(opcion == 4):
            pedi.menu()
        elif(opcion == 5):
            pa.menu()
        elif(opcion == 6):
            produ.menu()
        elif(opcion==0):
            break