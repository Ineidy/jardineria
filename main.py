import os
import module.getProductos as reportesproductos
import module.getClients as cli
import module.getOficina as of
import module.getEmpleados as empleado
import module.getpago as pa
import module.getPedidos as pedi
import module.postProduct as guardarproductos



def menuproductos():
    while True:
        os.system("clear")
        print("""
              
                                        ======================================

                                                BIENVENIDO AL REPORTE 
                                                          DE
                                                       PRODUCTOS 
                    
                                        ======================================
              




                            1. Reportes de productos
                            2. Edicion de productos
                            3.salir
              """)
        opcion= int(input("Ingrese la opcion deseada: "))
        if(opcion==1):
            reportesproductos.menu()
        elif(opcion==2):
            guardarproductos.menu()
        elif(opcion==3):
            break
            


if (__name__ == '__main__'):
    # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
    while True:
        print("""
              
                                        ======================================

                                                    MENU PRINCIPAL
                    
                                        ======================================  

              

              
                


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
            menuproductos()
        elif(opcion==0):
            break