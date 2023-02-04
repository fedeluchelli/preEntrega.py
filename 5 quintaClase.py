# num = 5
# while num>0:
#     print(f"{num}")
#     num -=1
# print("Terminó el conteo")


# for x in range(5):
#     print(x)


numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
opcion = "1"


while opcion == "1":

    print("""
    
        1- Opción suma
        2- Opción resta
        3- Opción multiplicación
        4- Salir
        
        """)
    opcion = input()

    if(opcion == "1"):
        print(f"La suma de los números es : {numero1 + numero2} "),
    elif(opcion =="2"):
         print(f"La resta de los números es : {numero1 - numero2} "),
    elif(opcion =="3"):
         print(f"La multiplicación de los números es : {numero1 * numero2} "),
    elif(opcion =="4"):
        print("Se está saliendo del programa")
        break
    else:
        print("La opción ingresada no es la correcta, vuelva a ingresar una de las opciones válidas")


#
# 
# 
#       Enumerate
#
#   como crear una lista rápida?
#       print(list(range(1,21)))

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# for pos, value in enumerate(lista):
#     print(f"pos: {pos} / value: {value}")

#       para que empiece a contar desde el 1

# for pos, value in enumerate(lista, 1):
#     print(f"pos: {pos} / value: {value}")