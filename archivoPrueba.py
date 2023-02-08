
############################################################################
#######################     PRUEBA ARMADO        ###########################
############################################################################


# import json

# data = {}
# data['Usuarios'] = []

# opcion = "1"
# while opcion == "1":
#     print("""
#           1- Ingresar usuario
#           2- Exportar base de datos a texto
#           3- Comprobar información
#           4- Log In
#           5- Salir
          
#           """)
#     opcion = input()

#     if (opcion == "1"):
#         data['Usuarios'].append({
#             'nombre' : input("Ingrese su nombre de usuario: "),
#             'password' : input("Ingrese su contraseña: ")
#         })
        
#     if (opcion == "2"):
#         with open("./experimento.txt", 'w') as file:
#             json.dump(data, file, indent=4)
#         opcion = input()
        
#     if (opcion == "3"):
#         print(data)
#         opcion = input()
        
#     if (opcion == "4"):
#         if(input("Ingrese su usuario: ") == ):
#             if(input("ingrese su contraseña: ") == 'password'):
#                 print("Acceso!");
#             else:
#                 print("Contraseña incorrecta, vuelva a intentarlo"),
#                 (opcion == "4");
#         else:
#             print("Usuario no existente, vueva a intentarlo"),
#             (opcion  == "4");    
            
#     if (opcion == "5"):
#         break

############################################################################
#######################      PRUEBA ARMADO 2      ##########################
############################################################################

# base_de_datos = {}
# count = 0

# def set_product():
#     index = count
#     while True:
#         nombre = input("Ingrese nombre del producto o 'S' para salir: ") 
#         if nombre.upper().strip() == "S":
#             break
#         precio  = float(input("Ingrese precio: "))
#         base_de_datos[index] = (nombre, precio)
#         index += 1

# def get_product(index) -> tuple:
#     if index in base_de_datos:
#         return base_de_datos[index]
#     return()

# def orchestrator():
#     while True:
#         option = input("1- Para cargar productos\n2- Para buscar productos")
    
#         if option == "1":
#             set_product()
            
#         elif option == "2":
#             index = int(input("Ingrese ID: "))
#             datos = get_product(index)
#             print(datos)

#         else:
#             print("Opción inválida")
            

# orchestrator()


############################################################################
#######################      PRUEBA ARMADO 2      ##########################
############################################################################


data_base = {}
count = 0
import json

def set_user():
    index = count
    while True:
        user = input("Ingrese nombre de usuario o presione 'S' para salir: ")
        if user.upper().strip() == "S":
            break
        password = input("Ingrese su contraseña: ")
        data_base[index] = (user, password)
        index += 1

def get_user(index) -> tuple:
    if index in data_base:
        return data_base[index]
    return()

def orchestrator():
    while True:
        option = input("""
                       ----------------------
                       1- Crear un usuario
                       2- Buscar usuario
                       3- Imprimir en .txt
                       4- Salir del programa
                       ----------------------
                       """)
        if option == "1":
            set_user()

        elif option == "2":
            index = int(input("Ingrese id: "))
            datos = get_user(index)
            print(datos)
        
        elif option == "3":
            with open("./experimento2.txt", 'w') as file:
                json.dump(datos, file, indent=4)
            
        elif option == "4":
            break

        else:
            print("Opción inválida")

orchestrator()
