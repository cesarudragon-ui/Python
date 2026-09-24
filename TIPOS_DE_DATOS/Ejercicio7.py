peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = round(peso / (estatura ** 2),2)
print(f"Tu índice de masa corporal es {imc}")