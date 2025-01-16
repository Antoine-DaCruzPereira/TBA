#capacité

class Capacite:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

    def __str__(self):
        return f"{self.name} ({self.type}) - Puissance: {self.power}"
