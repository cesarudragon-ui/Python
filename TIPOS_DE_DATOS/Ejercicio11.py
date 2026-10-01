inversion_inicial = float(input("Introduce la cantidad de dinero depositada: "))

interes = 0.04


balance_anio_1 = inversion_inicial * (1 + interes)
balance_anio_2 = balance_anio_1 * (1 + interes)
balance_anio_3 = balance_anio_2 * (1 + interes)

print("--- Resultados de tus ahorros ---")
print(f"Ahorros tras el 1.er año: {balance_anio_1:.2f} €")
print(f"Ahorros tras el 2.º año: {balance_anio_2:.2f} €")
print(f"Ahorros tras el 3.er año: {balance_anio_3:.2f} €")