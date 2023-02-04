
############################################################################
#######################     PRUEBA ARMADO        ###########################
############################################################################


import json

data = {}
data['Usuarios'] = []

opcion = "1"
while opcion == "1":
    print("""
          1- Ingresar usuario
          2- Exportar base de datos a texto
          3- Comprobar información
          4- Salir
          
          """)
    opcion = input()

    if (opcion == "1"):
        data['Usuarios'].append({
            'nombre' : input("Ingrese su nombre de usuario: "),
            'password' : input("Ingrese su contraseña: ")
        })
        
    if (opcion == "2"):
        with open("./experimento.txt", 'w') as file:
            json.dump(data, file, indent=4)
        opcion = input()
        
    if (opcion == "3"):
        print(data)
        opcion = input()
        
    if (opcion == "4"):
        break






