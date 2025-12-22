def correcion(cadena):
    if cadena.islower():
        cadena = cadena.capitalize()
        lista = list(cadena)
        lista.append(".")
    return "".join(lista)

pipi="hola como estas"
print(correcion(pipi))