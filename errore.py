try:

    entero = int(input("ingrese un numero: "))
except:
    print("El valor ingresado no es un numero")
else:
    print("La operacion es correcta")
    print(entero)
finally:
    print("puedes continuar")

