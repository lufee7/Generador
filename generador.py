# Eso es un generedor de contraseña basico! (Apenas un ejercicio, para poner en practica)

import random
import string

def generar_contraseña(nivel):
    if nivel == "Simple":
        longitud = 6
        caracteres = string.ascii_lowercase
    elif nivel == "Buena":
        longitud = 10
        caracteres = string.ascii_letters + string.digits
    elif nivel == "Hard":
        longitud = 16
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Nivel no válido. Usa: Simple, Buena o Hard.")
        return None

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Ejemplo de uso:
print("Niveles disponibles: Simple, Buena, Hard")
nivel = input("Elige el nivel de seguridad: ")
contraseña_generada = generar_contraseña(nivel)

if contraseña_generada:
    print("Aquí tiene tu contraseña segura:", contraseña_generada)
