# funciones avanzadas. Lo veré en la repetición poorque lo entendí, pero para fijarlo

# Funcióhn recursiva sin retorno

def cuenta_regresiva(numero):
    numero -=1
    if numero>0:
        print (numero)
        cuenta_regresiva(numero)
    else:
        print ("Booooooom!")
    print("Fin de la función", numero)

cuenta_regresiva(5)