
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario (€): "))
unidades = int(input("Número de unidades: "))

coste_total = precio * unidades

print(f"{producto}: {precio:09.2f}€ x {unidades:03d} unidades = {coste_total:011.2f}€")