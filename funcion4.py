def correcion(cadena):
    if cadena.islower():
        cadena = cadena.capitalize()
        lista = list(cadena)
        lista.append(".")
    return "".join(lista)

pipi="hola como estas."
print(correcion(pipi))

# Martu: Casi perfecto!! Solo faltaría una condición que analice en qué casos es  necesario agregar el punto al final.