#       ---              IF                 ---

# if True:
#     print("Se cumple!")

# edad = 12
# if edad>= 18:
#     print("Es un adulto"),
# else: 
#     print ("Es menor")

#           Chequeamops si el usuario existe e imprimimmos el resultaado.

# lista_usuario = ["Jose","Joel","Julia","Luz"]

# usuario = input("Ingrese nombre de  usuario: ")

# if usuario in lista_usuario:
#     print ("El usuario está")
# else:
#     print("El usuario no está")





#           ---     IF ANIDADO      ---

# lista_usuario = ["Jose","Joel","Julia","Luz"]
# lista_contrasenia=["abc","def","asd","123"]

# usuario = input("Ingrese nombre de  usuario: ")
# contrasenia = input("Ingrese su contraseña: ")

# if usuario in lista_usuario:
#     print ("El usuario está")

# #acá va hasta la lista, busca la posición y te devuelve la posición (por el indedx)
#     indice = lista_usuario.index(usuario)
# #para acá buscar esa contraseña y que coincida con la posición expresada 
#     if contrasenia == lista_contrasenia[indice]:
#         print("Ingreso correcto")
#     else:
#         print("Contraseña incorrecta")
# else:
#     print ("El usuario NO está")




#       ---     ELIF        ---

#   sigue buscando en la base de datos si la condición se cumple, no siendo por eso falsa

# a = 2+3
# if a == 4:
#     print("A es igual a cuatro")
# elif a ==5:
#     print("A es igual a cinco")
# elif a ==6:
#     print("A es igual a seis")
# else:
#     print("No se cumple la condición")

#Desafíos

#Primera opción

#anio = int(input("Ingrese el año de nacimiento: "))
# anio = 1993 #se le solicita al usuario un dato
# if anio >=1920 and anio<=1940:
#     print("Generación Silenciosa")
# elif anio>=1946 and anio<=1964:
#     print("Generación BabyBoomer!")
# elif anio>=1965 and anio<=1979:
#     print("Generación X")
# elif anio>=1980 and anio<=2000:
#     print("Generación Y")
# elif anio>=2001 and anio<=2010:
#     print("Generación Z")
# else:
#     print("No existe generación asociada")


#Segunda opción

# anio = int(input("Ingrese su año de nacimiento: "))
# generacion = str

# if anio >= 1920 and anio <= 1940:
#     generacion = "Generación silenciosa"
# elif anio >= 1946 and anio <= 1964:
#     generacion = "Baby boomer"
# elif anio >= 1965 and anio <= 1979:
#     generacion = "Generacion X"
# elif anio >= 1980 and anio <= 2000:
#     generacion = "Generacion Y"
# elif anio >= 2001 and anio <= 2010:
#     generacion = "Generacion Z"
# else: 
#     generacion = "No existe generacion asociada"
# print("Usted pertenece a: " + generacion)


#Opción avanzada

# def digital_generation (year):
#     generations = {
#         "Generacion_Silenciosa": range(1920, 1940),
#         "Baby_boomers": range(1946, 1964),
#         "Generacion_X": range(1965, 1979),
#         "Generacion_Y": range(1980, 2000),
#         "Generacion_Z": range(2001, 2010)
#     }

#     for generation, years in generations.items():
#         if year in years:
#             print(generation) 
#         else:
#             print("No se encuentra en ninguna generación")

# digital_generation(int(input("Ingrese el año de nacimiento: ")))
