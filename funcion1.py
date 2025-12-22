def pares(cadena): # Martu: Tal vez podrías poner un nombre más desscriptivo... :p
    inicio=0
    lista=[]
    if(len(cadena)%2==1):
        cadena+="_"

    while inicio<len(cadena):
        lista.append(cadena[inicio:inicio+2])
        inicio+=2
    return lista

cadena="hola"
print(pares(cadena))

# Martu: Excelente!!
