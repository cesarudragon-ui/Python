# Pedir los productos de la cesta separados por comas
cesta = input("Introduce los productos de la cesta de la compra (separados por comas): ")

# Separar la cadena por cada coma obteniendo una lista de productos
productos = cesta.split(",")

# Recorrer la lista y mostrar cada producto limpio de espacios en blanco sobrantes
print("\nProductos en tu cesta:")
for producto in productos:
    print(producto.strip())