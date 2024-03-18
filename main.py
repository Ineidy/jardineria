import os
import module.getClients as reportesclientes
import module.getOficina as reportesoficinas
import module.getpago as reportespagos
import module.getEmpleados as reportesempleados
import module.getPedidos as reportespedidos
import module.getProductos as reportesproductos
import module.postProduct as guardarproductos
import module.postOficinas as guardaroficinas
import module.postClientes as guardarclientes
import module.postpagos as guardarpagos
import module.postEmpleados as guardarempleados
import module.postPedidos as guardarpedidos


def menupedidos():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                                BIENVENIDO AL REPORTE 
                                                          DE
                                                        PEDIDOS 
                    
                                        ======================================
              
                            
              
                        1. Reportes de pedidos
                        2. Edicion de pedidos
                        0. salir
              
""")
        
        opcion = int(input("Seleccione una de las opciones"))
        if(opcion==1):
            reportespedidos.menu()
        elif(opcion==2):
            guardarpedidos.menu()
        elif(opcion==0):
            break


def menuempleados():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                                BIENVENIDO AL REPORTE 
                                                          DE
                                                       EMPLEADOS  
                    
                                        ======================================
              
                            
              
                        1. Reportes de empleados
                        2. Edicion de empleados
                        0. salir
              
""")
        
        opcion = int(input("Seleccione una de las opciones"))
        if(opcion==1):
            reportesempleados.menu()
        elif(opcion==2):
            guardarempleados.menu()
        elif(opcion==0):
            break


def menupago():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                                BIENVENIDO AL REPORTE 
                                                          DE
                                                         PAGO  
                    
                                        ======================================
              
                            
              
                        1. Reportes de pagos
                        2. Edicion de pagos
                        0. salir
              
""")
        
        opcion = int(input("Seleccione una de las opciones"))
        if(opcion==1):
            reportespagos.menu()
        elif(opcion==2):
            guardarpagos.menu()
        elif(opcion==0):
            break


def menuclientes():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                                BIENVENIDO AL REPORTE 
                                                          DE
                                                       CLIENTES 
                    
                                        ======================================
              
                            
              
                        1. Reportes de clientes
                        2. Edicion de clientes
                        0. salir
              
""")
        
        opcion = int(input("Seleccione una de las opciones"))
        if(opcion==1):
            reportesclientes.menu()
        elif(opcion==2):
            guardarclientes.menu()
        elif(opcion==0):
            break


def menuoficinas():
    while True:
        os.system("clear")
        print("""

                                        ======================================

                                                BIENVENIDO AL REPORTE 
                                                          DE
                                                       OFICINAS 
                    
                                        ======================================
              
                            
              
                        1. Reportes de oficinas
                        2. Edicion de Oficinas
                        0. salir
              
""")
        
        opcion = int(input("Seleccione una de las opciones"))
        if(opcion==1):
            reportesoficinas.menu()
        elif(opcion==2):
            guardaroficinas.menu()
        elif(opcion==0):
            break


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
                            0.salir
              """)
        opcion= int(input("Ingrese la opcion deseada: "))
        if(opcion==1):
            reportesproductos.menu()
        elif(opcion==2):
            guardarproductos.menu()
        elif(opcion==0):
            break
            


if (__name__ == '__main__'):
    # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
    while True:
        os.system("clear")
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
            menuclientes()
        elif(opcion == 2):
            menuoficinas()
        elif(opcion == 3):
            menuempleados()
        elif(opcion == 4):
            menupedidos()
        elif(opcion == 5):
            menupago()
        elif(opcion == 6):
            menuproductos()
        elif(opcion==0):
            break