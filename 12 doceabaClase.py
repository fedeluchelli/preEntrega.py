# Programación Orientada a Objetos

# si tengo un módulo lleno para manejar el stock, necesito que las demás cumplan la misma fórma
# es una forma de establecer cómo vamos a trabajar. Decidimos cómo vamos a resolver el problema

# PARADIGMAS
#
# 1. Imperativo
# archivo con código que se ejecuta paso a paso sin ningún tipo de variación. Simple porque no
# tiene funciones
# 
# 2. Declarativo
# opuesto al imperativo. Ej.: SQL
# una base de datos es un archivo de excel y cáda código una tabla (?)
# es declarativo porque se le dice que a la tabla A seleccione todo y haga una unión con la tabla B
# le decimos qué queremos de la tabla, NO PROGRAMAMOS QUE HACE. Simplemente le pedimos lo que 
# queremos, la actividad y que lo ejecute. Nos devuelve lo que le pedimos y no tenemos influencia en
# cómo lo hace
# 
# 3. Lógico
# lenguaje C (de más bajo nivel)


# Funcional: se componen de funciones, implementaciones ded comportamiento que reciben un conjuunto 
# de datos de entrada  y devuelven un valor de salida

# Orientado a objeto: El comportamiento del programa es llevado a cabo por objetos, entidades que 
# representan elementos del programa

# la programación orientada a objetos 
# 
# Ejemplos:

def obtener_producto():
    pass

def agregar_a_lista():
    pass

def eliminar_de_base():
    pass

def calcular_precio():
    pass

def calcular_precio_por_cantidad():     # Están todos sueltos, pero tienen una lógica común
    pass

def mostrar_lista():
    pass

def calcular_descuento():
    pass

def promo1():
    pass

def promo2():
    pass

def averigua_promo():
    pass

lista_codigos = []
lista_precios = []
lista_detalle = []
lista_unid_med = []

# Sintaxis para hacerlo con clases

class Producto:
    #el init es el constructor, el que da inicio a algo
    def __init__(self, codigo, precio, detalle, unid_med):  #self es una referencia al propio objeto
        self.codigo = codigo
        self.precio = precio
        self.detalle = detalle
        self.unid_med = unid_med    #con esto se generaron variables que puede utilizar toda la clase
        
    def muestra_detalle(self):
        print(f"{self.detalle} - {self.unid_med}: ${self.precio}")

producto1 = Producto("12312345", 155.0, "Coca-Cola", "1L")

producto1.muestra_detalle() #muestra_detalle es un método


# # # # # EJEMPLO EXTRA # # # # #

# def __init__(self)

# class Punto:
#         x=12
#         y=24

#         @classmethod
#         def imprimir(cls):
#             print("Coordenada del punto")
#             print("(",cls.x,",",cls.y,")")


# Punto.imprimir()