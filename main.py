import random
caracteres = "+-/*!&$=@AbcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("longitud de tu contraseña"))
resultado = ""

for i in range (longitud):
    resultado += random.choice(caracteres)

print(f"tu contraseña es: {resultado}")
