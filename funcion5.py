def inverso(cadena):
    palabras = cadena.split(' ')
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    return " ".join(palabras_invertidas)

pipi="hola mundo"
print(inverso(pipi))
