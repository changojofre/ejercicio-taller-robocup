def cuenta_puntos(cadena):
    contador = 0
    for caracter in cadena:
        if caracter == ".":
            contador += 1
        else:
            break
    return contador

cadena="......hola.como.estan?"
print(cuenta_puntos(cadena))
print(cuenta_puntos(cadena))

# Martu: Impecable!!
