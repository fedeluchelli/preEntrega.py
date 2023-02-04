
# Colección ordenada =/= desordenada

#   ordenada: tuplas - set - lista - string
#   desordenadas: diccionario - conjuntos
#       en el desorden no podemeos trabajar con referencia a orden
#       por más que el diccionario parezca ordenado, siempre es una colección
#       desordenada (por más que podamos encontrar todo)

#   Caracteristicas principales de un diccionario
#  _Dinámico : puede tener más diccionarios, listas, etc.
#  _Heterogéneo : no tiene necesidad de estar compuesto por 1 tipo de datos
#  _ Puede estar anidado : puede ser anidado hasta que nos de la ram
#  _Mutable

# La sintaxis para agregar un par llave valor a un diccionario es 
#               diccionario[llave] = valor

# Por qué necesitamos saber si es ordenada o no?
#     Lo necesitamos para saber cómo configurar algo


# Datos - mutables e inmutables
#   es inmutable un string? No, podemos acceder a una posición
#       pero no podemos cambiar su contenido. Podemos hacer 'trampa' y pisar
#       un valor nuevo, pero no podemos cambiar un string
#   ejemplo Inmutables : _Tuplas _Cadenas
# texto = "Hola Coder!"
# texto = "h" + texto[1:] #esto es slicing, no estás modificando el texto como modificación
# print(texto)

# En una lista podés hacer slicing o modificación
# no podés hacer slicing o modificar datos en desorden

# Si no es mutable, no podés modificar sus datos
# Si no está ordenado, debés pedir un dato a la vez

#   Cuando hacemos un slicing, necesitás que esté ordenado porque le estás marcando un principio
#   y un fin. NO TIENE QUE VER QUE SEA O NO MUTABLE


###############################################

#       Persistencia de datos       #

#   La persistencia es la posibildad de utilizar datos que fueron generados sea por nosotros
#   o algún agente. Es la acción de PRESERVAR información y también de poder RECUPERAR la informaicón
#   _ PRESERVAR = GUARDAR
#   _ RECUPERAR = LEER
#
#
#   En la base de datos hay muchos datos y variables (por ejemplo 'no relacionales')
#   y archivos, todo tipo de archivos es una forma de preservar datos (zip, jpg, excel, etc.)
#
#
#   Ahora usaremos SQLite. Es para archivos no importantes o pruebas, porque como no pide contraseñas
#   es de fácil acceso. Creando la base de datos le configuramos una contraseña, pero para otro tipo
#   de archivos.
#
#   a diferencia de los archivos binarios u otro tipos de archivos que contienen datos, que necesitan
#   ciertas formas de configuración, por lo que se debe conocer para poder modificar.
#
#
#
#       OPEN - es la extensión que se usa para abrir archivos
#
#   Generalmente un 'f' es de 'find' y refiere a un archivo
#   La particularidad de OPEN es que busca ESE archivo en ESA ruta
#   si está lo abre y si no está lo crea.
#       f = open(ruta + "/archivo,txt", "W")
#   podemos hacer una escritura sobre ese archivo y luego CERRAR ese archivo, porque
#   sino no puede abrirse con otro programa poqrue Windows no permite abrir 2 veces 
#   un archivo en ejecución. Python lo cierra, pero lo ideal es cerrarlo nosotros.
#       f.write("Esto es un texto.")
#       f.close()


#       Así creamos un archivo! Que buena onda !!
# file = open("./mi archivo de texto.txt", "w")
# file.write("Hola clase 8")
# file.close()


# texto = "Hola clase 08 - 23-01-2023"
# file = open("./mi archivo de texto.txt", "w") # w = escribir
# file.write(texto)
# file.close()

# texto = "Hola clase 08 - 23-01-2023"
# file = open("./mi archivo de texto.txt", "a") # a = append
# file.write(texto)
# file.close()


# print("Hola mundo!")
# # 1- Abrir o crear      -       pide 2 argumentos QUE DEBEN SER STRING
# archivo = open("./hobbies.txt", "w")

# # 2- Escribir la info
# misHobbies = ""
# # hobby1 = input("Ingresa tu hobby favorito")
# # hobby2 = input("Ingresa tu segundo hobby favorito")
# # hobby3 = input("Ingresa tu tercer hobby favorito")
# #   en vez de así, se puede usar un FOR
# for i in range(3):
#     hobbies = input("Ingrese hobby: ")
#     misHobbies = misHobbies + " " + hobbies
# archivo.write(misHobbies)

# # 3- Cerrar (guardar) el archivo
# archivo.close()

# #   Con 'a' (de append) se agrega la información, pero aparecería pegada. A menos que
# #   se agregue un salto de línea con un \n
# texto = "\nHola clase 08 - 23-01-2023"
# file = open("./mi archivo de texto.txt", "r") # a = append
# # file.write(texto)
# # file.close()

# # Para borrar y escribir nuevamente se debe escribir solo 'w'
# for line in file.readlines():
#     print(line)

# file.close()

#########################################################
#       Archivo JSON        #

#   un JSON es un gran directorio (es similar a un diccionario)
#   la diferencia es que el JSON tiene más limitaciones
#   a partir de un diccionario propio nos permite tener un JSON
#   y viceversa.


# texto = "nombre = input('Ingrese un nombre: ')"
# texto += "\nprint(nombre)"

# f = open("./archivo.py", "w")

# f.write(texto)
# f.close()