class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor, marca, modelo):
        self.motor = motor
        self.marca = marca
        self.modelo = modelo

motor_gasolina = Motor("Gasosa", 180)

carro_gasolina = Carro(motor_gasolina, "Toyota", "Supra MK2")

print(f"Carro: {carro_gasolina.marca} {carro_gasolina.modelo}")
print(f"Motor: Tipo: {carro_gasolina.motor.tipo}, Potência: {carro_gasolina.motor.potencia} Cavalos")
