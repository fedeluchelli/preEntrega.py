
# Se debe crear un diccionario que almacene 
# Función que lea y que ante coincidencia en la base de datos (diccionario)

# Que almacene datos Y SE PUEDA LEER

# se puede jugar con un txt. O QUE SE GUARDE EN UN JSON <-- b u s c a r ! !

# tirar errores ante fallas con el login
# Si se puede usar PARÁMETROS - RETURN mejor


################################################################################
############################     PRUEBA 1        ###############################
################################################################################
# opcion = "1"

# while opcion == "1":

#     print("""
    
#         1- Registrarse
#         2- Login
#         3- Eliminar usuario
#         4- Salir
        
#         """)
#     opcion = input()

#     if(opcion == "1"):
#         def escribir():
#         ,
#     elif(opcion =="2"):
#         ,
#     elif(opcion =="3"):
#          print(f"La multiplicación de los números es : {numero1 * numero2} "),
#     elif(opcion =="4"):
#         print("Se está saliendo del programa")
#         break
#     else:
#         print("La opción ingresada no es la correcta, vuelva a ingresar una de las opciones válidas")

# BD = {}

# dándolo vuelta funciona la búsqueda mediante GET
# db1={
#     input("Ingrese su nombre: "): "Usuario1",
#     input("Ingrese su password: "):"PassUsuario1"  
# }
# con esto se puede ver si usuario está en base de datos y dice el número
# print(db1.get(input("Ingrese el usuario que desea buscar: "), "El usuario no existe en la base de datos"))

# con esto confirmo que se agregó al diccionario general #
# BD.update(db1)

# def leer():
#     print(BD)
# leer()

# BD = {}
# while True:
#     operacion = input("""
#                       1- guardar un usuario
#                       2- eliminar usuario
#                       3- actualizar usuario
#                       4- salir
#                       """)
    
#     Usuario = input("Ingrese su nombre de usuario: ")
#     Password = input("Ingrese su password: ")

    
#     if (operacion == "1"):
#         BD = {
#             "Usuario" : Usuario,
#             "Password" : Password
#         }


################################################################################
############################     PRUEBA 2        ###############################
################################################################################



# usuarios = {
#     "Fede" : "contra1",
#     "Emma" : "contra2",
#     "Rebeca" : "contra3"
    
#     }

# r = usuarios.keys()
# p = usuarios.values()
# print(r)
# print(p)





# for users in usuarios.values():
#     if users == input("Ingrese su contraseña: "):
#         print(users)


# for llave in usuarios.keys():
    
#     print(usuarios[llave])


# print(BD)

# r = usuarios.get("usuario")

# r = usuarios.values()
# print(r)

################################################################################
############################     PRUEBA 3        ###############################
################################################################################


# usuarios = {
#     input("Ingrese su nombre de usuario: "):input("Ingrese su contraseña: "),
#     input("Ingrese su nombre de usuario: "):input("Ingrese su contraseña: ")
#     }

# for users in usuarios.keys():
#     print(users)
# for password in usuarios.values():
#     print(password)


# for users, password in usuarios.items():
#     if input("Ingrese su usuario: ") == users:
#         if input("Ingrese su contraseña: ") == password:
#             print("Acceso!")
#         else:
#             print("Contraseña equivocada")
#     else:
#         print("Usuario no registrado")

# texto = str(usuarios)

# file = open("./archivoBaseDatos.txt", "w")
# file.write(texto)


################################################################################
############################     PRUEBA 4        ###############################
################################################################################


# BD = {}

# while True:
#     operacion = input("""
#                       1- guardar un usuario
#                       2- eliminar usuario
#                       3- actualizar usuario
#                       4- salir
#                       """)
    
#     Usuario = input("Ingrese su nombre de usuario: ")
#     Password = input("Ingrese su password: ")

    
#     if (operacion == "1"):
#         usuario1 = {
#             "Nombre": Usuario, 
#             "Password": Password
#         },BD.update(usuario1),
#         print("Usuario registrado!") 
        

# nombre = input("Ingrese su nombre: ")
# contra = input("Ingrese su contraseña: ")



# usuario2 = {
#     "Nombre": nombre, 
#     "Password": contra
#     }
# BD.update(usuario2)

# print(BD)

# file = open("./archivoBaseDatos.txt", "w")
# file.write(str(BD))

################################################################################
############################     PRUEBA 5        ###############################
################################################################################

# # 1- Abrir o crear el .txt

# file = open("./archivoBaseDatos.txt", "w")

# # 2- Escribir la info

# baseDatos = {}

# for i in range(3):
#     usuario = input("ingrese nombre de usuario: ")
#     password = input("ingrese su contraseña: ")
#     baseDatos = usuario + " " + password

# file.write(str(baseDatos))

import json

data = {}
data['Usuarios'] = []

data['Usuarios'].append({
    'nombre' : input("Ingrese su nombre de usuario: "),
    'password' : input("Ingrese su contraseña: ")
})

data['Usuarios'].append({
    'nombre' : input("Ingrese su nombre de usuario: "),
    'password' : input("Ingrese su contraseña: ")
})

print(data)

with open("./experimento.txt", 'w') as file:
    json.dump(data, file, indent=4)

input()