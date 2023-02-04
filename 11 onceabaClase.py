#       EXCEPCIONES

# Son bloques de código que nos permiten continuar con la ejecución
# pese a que está ocurriendo un error

# TRY & EXCEPT              // El except es OBLIGATORIO que esté

# try:
#     n = float(input("ingresar n:\n"))
#     m = 4
#     print(f"----> {n}/{m} = {n/m}")
# except:
#     print("Algo salió mal!!!")

# Cómo saber donde está el error? Acá hay un solo lugar donde el error puede recidir
# por tanto es preferible escribir el código así

# try:
#     n = float(input("ingresar n:\n"))
# except:
#     print("Algo salió mal!!!")
# m = 4
# print(f"----> {n}/{m} = {n/m}")

# Si veo que el bloque está bien definido y el error puede estar en un solo lugar
# ahí es donde se debe utilizar el try&except
# mientras más específico seamos mejor

#       ELSE

#       FINALY

# la sentencia try tiene otra sentencia opcional  que intenta definir acciones de 
# limpieza que deben ser  ejecutadas bajo ciertas circunstancias. Una sentencia
# finaly SIEMPRE ES EJECUTADA ANTES DE SALIR DE LA SENTENCIA  TRY, ya sea que una
# excepción haya ocurrido o no

# try:
#     n= float(input("Ingrese un valor: "))
# except:
#     print("Este valor es inválido para la operación")
# else:
#     print("Esto se ejecuta si salió todo bien")
# finally:
#     print("Esto lo vas a ver siempre")

# print("Fin del programa")

# Hay distintos tipos de errores que se pueden dar y mediante distintas excepciones podemos saber cual

try:
    n=float(input("Introduce un número  divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número en una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("Debes introducir un número distinto de cero")
except Exception  as e:
    print("Ha ocurrido un error no previsto", type(e).__name__)