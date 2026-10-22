key = "contraseña"
user_password = input("Introduce la contraseña: ")

if key.lower() == user_password.lower():
    print("La contraseña coincide.")
else:
    print("La contraseña no coincide.")