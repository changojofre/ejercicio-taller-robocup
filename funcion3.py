def mas_cercano(conjunto, numero):
    mas_cercano= list(conjunto)[0]
    menor_distancia= abs(mas_cercano - numero)
    
    for numero in conjunto:
        dist_actual= abs(mas_cercano - numero)

        if dist_actual < menor_distancia:
            menor_distancia = dist_actual
            mas_cercano = numero
    return mas_cercano

datos = {4, 6, 9, 15, 12}
print(mas_cercano(datos, 5))
