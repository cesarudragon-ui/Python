numeros1 = int(input("ingrese el primer numero:"))
numeros2 = int(input("ingrese el segundo numero:"))


numeros_dividir = numeros1/numeros2

if numeros_dividir == 0:
    print("ERROR")
else:
    print("El resultado de la división es :", numeros_dividir)