class Perro:
    def __init__(self, color, nombre, raza):
        self.color= color
        self.nombre= nombre
        self.raza= raza
        self.edad= 0  
        self.hambre= 3 

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")
        print(f"Edad: {self.edad}")
        print(f"Nivel de Hambre: {self.hambre}/5")

    def felizCumple(self):
        
        self.edad+= 1
        print(f"¡Feliz cumple! {self.nombre} Ahora tiene {self.edad} años.")

    def alimentar(self, cantidad):
        
        self.hambre-= cantidad
       
        if self.hambre< 0:
            self.hambre= 0
        
        if self.hambre== 0:
            print(f"{self.nombre} dice: ¡Estoy Lleno!")
        else:
            print(f"{self.nombre} comio {cantidad}. Su hambre ahora es {self.hambre}/5.")

perro1= Perro("Marrón", "Ricardo", "Salchicha") #como el de mi tia :D

perro1.mostrar_info()

perro1.felizCumple()
perro1.mostrar_info()

perro1.alimentar(2) 

# Martu: Muy bien! También podrías reemplazar el método mostrar_info con un método __str__ :)