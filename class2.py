class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
        self.pi = 3.1415

    def calcular_area(self):
        return self.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * self.pi * self.radio

circulo = Circulo(5)


area = circulo.calcular_area()
print(f"El área del círculo es: {area:.2f}")

perimetro = circulo.calcular_perimetro()
print(f"El perímetro del círculo es: {perimetro:.2f}")