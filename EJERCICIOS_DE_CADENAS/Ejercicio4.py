telefono = input("Introduce un número de teléfono con el formato +34-número-extensión: ")

partes = telefono.split("-")
print("El número de teléfono es:", partes[1])