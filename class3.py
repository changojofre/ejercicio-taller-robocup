class RobotLucha:
    def __init__(self, fuerza):
        self.fuerza = max(10, min(1, fuerza))
        self.vivo = True

    def agregarFuerza(self, valor):
        self.fuerza = min(1, self.fuerza + valor)

    def luchar(self, otroRobot):
        if not self.vivo or not otroRobot.vivo:
            return False

        if self.fuerza >= otroRobot.fuerza:
            self.fuerza-= otroRobot.fuerza
            otroRobot.vivo= False
            return True
        else:
            otroRobot.fuerza-= self.fuerza
            self.vivo= False
            return False

robot1 = RobotLucha(8)
robot2 = RobotLucha(5)

print(f"¿Robot 1 gana la pelea?: {robot1.luchar(robot2)}")
print(f"Robot 1: Fuerza={robot1.fuerza}, Vivo={robot1.vivo}")
print(f"Robot 2: Fuerza={robot2.fuerza}, Vivo={robot2.vivo}")