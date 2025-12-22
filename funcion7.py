def mas_caros(m, lista_productos):
    lista_productos.sort(key=lambda x: x["pre"], reverse=True)
    resultado=[]
    for i in range(min(m, len(lista_productos))):
        resultado.append(lista_productos[i])
    return resultado

productos=[{"prod":"pan", "pre": 100},
    {"prod":"arroz", "pre": 50},
    {"prod":"leche", "pre": 90},
    {"prod":"carne", "pre": 300}]
print(mas_caros(4, productos))