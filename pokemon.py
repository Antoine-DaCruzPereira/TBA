#pokemon

class Pokemon:
    def __init__(self, name, type1, type2, pv, attack, defense, speed, moves):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.pv = pv
        self.max_pv = pv
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves  

    def is_fainted(self):
        return self.pv <= 0

    def take_damage(self, damage):
        self.pv -= damage
        if self.pv < 0:
            self.pv = 0

    def __str__(self):
        return f"{self.name} ({self.type1}/{self.type2}) - {self.pv}/{self.max_pv} HP"
