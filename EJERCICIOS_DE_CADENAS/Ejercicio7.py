correo = input("Esccribe tu correo:")

nombre_usuario = correo.split("@") [0]
nuevo_correo = nombre_usuario + "@ceu.es"

print(f"Tu nuevo correo {nuevo_correo}")