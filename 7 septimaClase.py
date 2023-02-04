#       CADENAS Y STRINGS

# cadena1 = "Hola Mundo! Esta cadena tiene muchas o a *********"
# cadena2 = ["10", "10", "2023"]

# resultado = cadena1.upper()
# resultado = cadena1.lower()
# resultado = cadena1.capitalize() #mayus al primer
# resultado = cadena1.title() #pone mayuscula al primer caracter
# resultado = cadena1.count("Esta") #es key sensitive
# resultado = cadena1.find("o") #busca la posición
# resultado = cadena1.rfind("o") #busca la última posición
# resultado = cadena1.split() #hace un string y separa palabra por palabra
                              #puede ser separado mediante lo que se especifique dentro del paréntesis
# resultado = cadena1.join() #une lo que esté adentro con guiones
# resultado = "/".join(cadena2) #une lo que esté ahí dentro
# resultado = cadena1.strip("*") #quita cosas, como por ejemplo acá el asterisco
# resultado = cadena1.replace("*****", " ") #reemplaza los caracteres de una cadena
                                            #con lo que le digamos. Ej. 5 asteriscos con 1 espacio
                                            #podés poner mediante una coma más, cuantas veces se ejecute


# print(resultado)

# lista1 = [1, 2, 4]
# lista2 = [4, 5, 6]
# lista3 = ["a", "B", "A", "b"]

# lista1.extend(lista2) #agrega
# lista1.insert(2,3) #inserta en la posición 2, el número 3
#lista1.insert(len(lista1),"Hoola") #así se puede agregar string. Sin len no funciona!
                                    #lista1.insert("Hola") = MAL!!!
# lista3.sort() #ordena

# print(lista3)

#       #       #       #       #       #       #

#       CONJUNTOS

# cada uno de sus valores es individual y agrupamos los valores por llaves
# set1 = {1,2,3}
# set2 = {3,4,5}
#diferente del diccionario que a yellow le equivale 'amarillo'
#   diccionario = {"yellow": "amarillo"}

# set3 = set1.copy()
# print(set3)

# set5 = {4,5,6}
# set6 = {2,3}
# set5.issuperset(set6)
# print(set6)


#       DICCIONARIO

# con GET se puede agregar datos para que no se pinche la operación
# colores = {
#     "amarillo":"yellow",
#     "azul": "blue",
#     "verde": "green"
# }
# r = colores.get("negro", "Falso")
# print(r)

# Entrar con bucle
# colores = {
#     "amarillo":"yellow",
#     "azul": "blue",
#     "verde": "green"
# }

# for llave in colores.keys():
#     print(colores[llave]) #imprime value
#     #print(llave)

# for valores in colores.values():
#     if valores != "green":
#         print(valores)

# for valores in colores.values():
#     print(valores)  #así imprime tuplas

# for llave, valor in colores.items():
#     if valor != "blue":
#         print(llave)