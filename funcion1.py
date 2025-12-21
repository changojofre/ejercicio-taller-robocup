def pares(cadena):
    inicio=0
    lista=[]
    if(len(cadena)%2==1):
        cadena+="_"

    while inicio<len(cadena):
        lista.append(cadena[inicio:inicio+2])
        inicio+=2
    return lista

cadena="dabale arroz a la zorra del abad"
print(pares(cadena))
