import storage.oficina as of
from tabulate import tabulate

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
        "codigo_oficina": val.get("codigo_oficina"),
        "ciudad": val.get("ciudad")
        })

    return codigoCiudad


def getAllCiudadTelefono(pais):
    ciudadTelefono =[]
    for val in of.oficina:
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono":val.get("telefono"),
                "oficina":val.get("oficina"),
                "pais":val.get("pais")
            })
            

def menu():
    print("""
 
   ___  _______  ____  ___  ______________  ___  ____  ____  __________________  _____   ____
  / _ \/ __/ _ \/ __ \/ _ \/_  __/ __/ __/ / _ \/ __/ / __ \/ __/  _/ ___/  _/ |/ / _ | / __/
 / , _/ _// ___/ /_/ / , _/ / / / _/_\ \  / // / _/  / /_/ / _/_/ // /___/ //    / __ |_\ \  
/_/|_/___/_/   \____/_/|_| /_/ /___/___/ /____/___/  \____/_/ /___/\___/___/_/|_/_/ |_/___/  
                                                                                             

                            
                            1.
                            2.
                            3.
                            4.
                            5. 


    """)