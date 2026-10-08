fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

dia = fecha.split("/")[0].zfill(2)
mes = fecha.split("/")[1].zfill(2)
anio = fecha.split("/")[2].zfill(2)

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")