import math
from abc import ABC, abstractmethod
class figura(ABC):
    @abstractmethod
    def area(self):
        pass 

    @abstractmethod
    def perimetro(self):
        pass
    def __str__(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimetro={self.perimetro():.2f}"
    #el ejercicio 6 seria esto de arriba no?
class circulo(figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio
    
class cuadrado(figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado
    
class rectangulo(figura):
    def __init__(self, ancho, alto):
        self.base = ancho
        self.altura = alto

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2
    
class rombo(figura):
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.D = diagonal_mayor
        self.d = diagonal_menor
        self.lado = lado

    def area(self):
        return (self.D * self.d) / 2
    def perimetro(self):
        return 4 * self.lado
    
class trapecio(figura):
    def __init__(self, base_mayor, base_menor, lado1, lado2, altura):
        self.B = base_mayor
        self.b = base_menor
        self.lado1 = lado1
        self.lado2 = lado2
        self.h = altura

    def area(self):
        return ((self.B + self.b) * self.h) / 2

    def perimetro(self):
        return self.B + self.b + self.lado1 + self.lado2
    #no entiendo lo de poligono :(

print (circulo(5))
print (cuadrado(4))
print (rectangulo(4,6))
print (rombo(6,4,5))