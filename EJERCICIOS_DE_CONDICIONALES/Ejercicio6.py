nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M para mujer, H para hombre)? ")

inicial = nombre[0].upper()
sexo = sexo.upper()

if (sexo == "M" and inicial < "M") or (sexo == "H" and inicial > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Tu grupo es el {grupo}.")