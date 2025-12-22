def cuenta_puntos(cadena):
    contador = 0
    for caracter in cadena:
        if caracter == ".":
            contador += 1
        else:
            break
    return contador

cadena="......hola.como.estan?"
<<<<<<< HEAD
print(cuenta_puntos(cadena))
=======
print(cuenta_puntos(cadena))

# Martu: Impecable!!
>>>>>>> 92ea6f428ed16d6cb84719ae9ea2317e168c9ba8
