
#       FUNCIONES       #



#las funciones le ponen un título a un código para que después se ejecute
# debe poder distinguirse de otros patrones
# def nombre():
#     edad = 30
#     nombre = "Fede"
#     print("Mi nombre es %s y mi edad es %s" %(nombre, edad))

# #siempre que vamos a llamar a una función hay que ponerle paréntesis
# print(nombre())

#Función es agarrar un pedazo de código y encapsularlo en un nombre 
#   para así poder llamarlo
#       DEF es cómo decirle a py que es una función

# lista = [1,2,3]

# def largo(lista):
#     for index, value in enumerate(lista,1):
#         pass
#     print(index)

# largo(lista)

# def nombre(edad, nombre):
#     if True:
#         print("Mi nombre es %s y mi edad es de %s años" %(nombre, edad))

# edad_ingresada = int(input("Edad: "))
# nombre_ingresado = input("Nombre: ")

# nombre(edad_ingresada, nombre_ingresado)
# input()

##      ejercicio de clase      ##

def es_multiplo(n1, n2):
    if(n1 % n2 ==0):
        print(f"El número {num_1} es múltiplo de {num_2}");
    elif(n2 % n1 ==0):
        print(f"El número {num_2} es múltiplo de {num_1}");
    else:
        print("Ninguno es múltiplo del otro")

num_1 = int(input("ingrese un numero: "))
num_2 = int(input("ingrese un numero: "))

es_multiplo(num_1, num_2)
print("Presione ENTER para cerrar")
print("O podés dejarlo así abierto que está todo bien")
input()
##############################  con return! ##########################
# def es_multiplo(n1, n2):
#     if n1 % n2 ==0:
#         return f"El número {num_1} es múltiplo de {num_2}";
#     elif n2 % n1 ==0:
#         return f"El número {num_2} es múltiplo de {num_1}";
#     else:
#         print("Niinguno es múltiplo del otro")

# num_1 = int(input("ingrese un numero: "))
# num_2 = int(input("ingrese un numero: "))

# print(es_multiplo(num_1, num_2))