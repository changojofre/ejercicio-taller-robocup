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
print(mas_cercano(datos, 10))

# Martu: Revisar la lógica... hay un error de nombres en el for, que hace que se mezclen las variables individuales
# de la lista con el valor que pasa como parámetro. Por eso el resultado no es el esperado. :p. Solucionando eso, el
# ejercicio estaría perfecto!
