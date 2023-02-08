# import json

# users = {}

# def register_user(username, password):
#     users[username] = password
#     print("Usuario registrado exitosamente.")

# def display_users():
#     print("Usuarios registrados:")
#     for username in users:
#         print(username)

# def login(username, password):
#     if username in users:
#         if users[username] == password:
#             print(f"Bienvenido {username}!")
#         else:
#             print("Error en la contraseña")
#     else:
#         print("Error de inicio de sesión")   
 

# opcion = "1"
# while opcion == "1":
    
#     print("""
#           ----------------------------------
#           1- Ingresar usuario
#           2- Log In
#           3- Visualizar información
#           4- Exportar base de datos a texto
#           5- Salir
#           ----------------------------------
#           """)
    
#     opcion = input()

#     if (opcion == "1"):
#         register_user(input("Cree su usuario: "), input("Cree su contraseña: "))
    
#     if (opcion == "2"):
#         login(input("Usuario de acceso: "), input("Ingrese su contraseña: ")), 
#         opcion = input()
        
#     if (opcion == "3"):
#         display_users(),
#         opcion = input()
        
#     if (opcion == "4"):
#         with open("./experimento.txt", 'w') as file:
#             json.dump(users, file, indent=4)
#         opcion = input()

#     if (opcion == "5"):
#         break











import json

users = {}

def register_user(username, password):
    users[username] = password
    print("Usuario registrado exitosamente.")

def display_users():
    print("Usuarios registrados:")
    for username in users:
        print(username)

def login(username, password):
    if username in users:
        if users[username] == password:
            print(f"Bienvenido {username}!")
            return True
        else:
            print("Contraseña incorrecta")
            return False
    else:
        print("Usuario no registrado")
        return False   
 
def display():
    opcion = "1"
    while opcion == "1":
        
        print("""
            ----------------------------------
            1- Ingresar usuario
            2- Log In
            3- Visualizar información
            4- Exportar base de datos a texto
            5- Salir
            ----------------------------------
            """)
        
        opcion = int(input())

    if (opcion == 1):
        register_user(input("Cree su usuario: "), input("Cree su contraseña: ")),
        display()
    
    if (opcion == 2):
        login(input("Usuario de acceso: "), input("Ingrese su contraseña: ")), 
        display()
        
    if (opcion == 3):
        display_users(),
        display()
        
    if (opcion == 4):
        with open("./experimento.txt", 'w') as file:
            json.dump(users, file, indent=4)
        display()

    # if (opcion ==  5):
    #     break

display()


































