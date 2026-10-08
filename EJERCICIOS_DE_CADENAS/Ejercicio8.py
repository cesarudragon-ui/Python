precio = input("Escribe el precio en € con decimales:")

Euros = precio.split(".")[0]
Centimos = precio.split(".")[1].ljust(2, "0")

print(f"Los euros son {Euros} y los centimos {Centimos}")