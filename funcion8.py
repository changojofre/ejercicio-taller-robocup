def segunda_pos(c1, c2):
    primera= c1.find(c2)
    if primera == -1:
        return None
    segunda= c1.find(c2)
    return segunda if segunda != -1 else None

print(segunda_pos("esto es una estatua", "st"))