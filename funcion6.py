def digitos(cadena):
    contador = 0
    for caracter in cadena:
        if "0" <= caracter <= "9":
            contador += 1
    return contador

ej= "compre una docena de empanadas, 4 de carne, 3 de jyq, 3 de pollo y 2 de hunita"
print(digitos(ej))

# Martu: TODO (opcional): rehacer tratando de resolverlo usando un método ya existente de python para identificar si un caracter es
# un dígito... :) (de paso, el método funciona igual :) )