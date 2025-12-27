def segunda_pos(c1, c2):
    primera= c1.find(c2)
    if primera == -1:
        return None
    segunda= c1.find(c2)
    return segunda if segunda != -1 else None

print(segunda_pos("esto es una estatua", "st"))

# Martu: Está casi perfecto, pero al buscar la segunda aparición de c2 desde el comienzo de c1, lo que pasa es que
# siempre va a encontrar la primera, recordá que find devuelve el índice de la primera aparición, en este caso, de c2
# en c1. Pista: Revisá qué parámetros tiene el método find, ¿podrías decirle a find desde qué índice comenzar a buscar :)?