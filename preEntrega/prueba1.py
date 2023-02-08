############################################################################
#######################      PRUEBA ARMADO 2      ##########################
############################################################################


data_base = {}

import json

def set_user(count):
    index = count
    while True:
        user = input("Ingrese nombre de usuario o presione 'S' para salir: ")
        if user.upper().strip() == "S":
            break
        password = input("Ingrese su contraseña: ")
        data_base[index] = (user, password)
        index += 1
        return index

def get_user(index) -> tuple:
    if index in data_base:
        return data_base[index]
    return()

def orchestrator():
    count = 0
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
            count = set_user(count)

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