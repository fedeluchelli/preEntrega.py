#############   CONJUNTOS    #############
#
#    colección no ordenada de objetos únicos y al ser 'no ordenada'
#    nos prohibe hacer ciertas cosas no podremos acceder
#    con un número, podemos ver todos los elementos, pero no se accede
#    de esa manera.
#    Nos permite poner strings, numbers o tuplas. NO permite diccionarios o listas
#    NO SE PUEDE PONER CONJUNTOS VARIABLES
#
#
#
#   Ejemplo de conjunto
#   se puede crear mediante

# mi_set = set()
# lista=list()
# lista2=[]
#   (lo corroboramos con type)
#
# print(type(lista2))
#
#
#    NO REPITE! Omite el repetido, quedándose con el primero
#
#
# conjunto1 = {1,2,"Juan","Juan"}
# print(conjunto1)
#
#    Podemos agregar datos!
#
# conjunto1.add("Nadia")
# print(conjunto1)
#
#    Podemos actualizar un elemento
# conjunto1.update([33,12,"Miguel"])
# print(conjunto1)
#
#
#    Sacamos valores
# conjunto1.discard(33)
# print(conjunto1)
#
#
#    Podemos con REMOVE eliminar elementos y lo especial es que
#    si el elemento no está lanza error, haciéndonos saber
#    que ese elemento NO ESTÁ por lo que no se puede eliminar.
#       -   (con discard si el elemento no está, no te avisa)
#
# conjunto1.remove("Lucas")
# print(conjunto1)
#
#
#
#    Podemos eliminar todo  con CLEAR
#
#
#
#
#
#           EJERCITACIÓN RÁPIDA
#
# colores = {"Rojo", "Blanco", "Azul"}
# print(colores)
# print(type(colores))


#   Agregar Violeta y Dorado
#
# colores.add("Violeta")
# colores.add("Dorado")
#
#   sino podríamos agregarlo como una lista
#
# colores.update(["Violeta", "Dorado"])
# print(colores)
# print(type(colores))


#   Eliminar color Violeta
#
# colores.discard("Violeta")
# print(colores)
# print(type(colores))

#
#
#
#
#
#############   DICCIONARIO    #############
# 
# 
#   Colección NO ordenada de objetos
#   para identificar un valor especificamos una clave
#   suelen ser entros (int) o string
#
#   Se emplean llaves vacías
#       diccionario = {}
#
#   No podés tener 2 valores en una key
#   y si le ponés coma lo toma como otra key
#
# colores = {
#     "Amarillo": "Yellow",
#     "Azul": "Blue", 
#     "Rojo": "Red"
#     }

# print (colores)
# print(colores["Amarillo"])

#   Podemos cambiar un dato
# colores["Amarillo"] = "Bla Bla"
# print(colores["Amarillo"])
# print(colores)

#   Dentro de los diccionarios no existen claves iguales
#   si la clave no existe se agrega y si existe se pisa
# colores.update({"Rojo": "Green"})
# print(colores)
#   también se puede hacer así
# colores["Amarillo"] = "Violeta"
# print(colores)

#   Len -   busca el largo del diccionario
# print(len(colores))

#   Del -   eliminamos
# del colores["Rojo"]
# print(colores)

#   Saber si hay valores
# print("Azul" in colores)

#   Se pueden poner diccionarios dentro del diccionario
# colores = {
#     "Amarillo": {"Yellow": 15},
#     "Azul": "Blue", 
#     "Rojo": "Red"
#     }
# print(colores)



#
#
#
#
#
#############   EJERCITACIÓN    #############
# 
# 
#   1) Crear nuestro propio diccionario con nuestro código
#   cargándole datos generales y dentro de otra key ponemos
#   otros diccionarios que se agregaron
#
#   2) Ingresando los items que se van comprando
#   y realizando la suma del total
#
#   3) Teniendo una diferenciación si se paga al contado
#   o con tarjeta

base_datos = {
    "100": {"detalle": "ARROZ","precio": 50,"cantidad": 2,},
    "101": {"detalle": "FIDEOS","precio": 0.5,"cantidad": 1,},
    "102": {"detalle": "PURE DE TOMATE","precio": 125,"cantidad": 2,},
    "103": {"detalle": "MAYONESA","precio": 10.5,"cantidad": 1,},
    "104": {"detalle": "COCA","precio": 150,"cantidad": 2,},
    "105": {"detalle": "BRANCA","precio": 120.5,"cantidad": 1,},
    "106": {"detalle": "CERVEZA","precio": 550,"cantidad": 2,},
    "107": {"detalle": "PAN","precio": 860.5,"cantidad": 1,},
    "108": {"detalle": "QUESO","precio": 50,"cantidad": 2,},
    "109": {"detalle": "AGUA","precio": 90.7,"cantidad": 1,}
    }

base_datos = { }

while True :

    operacion = input("""
                        1- Guardar producto
                        2- Eliminar un producto
                        3- Actualizar un producto
                        4- Mostrar productos de la lista
                        5- Registrar venta
                        6- Salir
                        """)

    if(operacion =="1"):

            identificador = input("Ingrese el identificador del producto: ")
            detalle = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad de productos: "))

            base_datos = {
                identificador: {
                    "detalle" : detalle,
                    "precio" : precio,
                    "cantidad" : cantidad,
                }
            }

    elif(operacion =="4"):
            print(base_datos)
    elif(operacion =="6"):
            break