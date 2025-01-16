#pokemon
import random

class Pokemon:
    def __init__(self, name, type1, type2, describe, stats, capacites=None):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.describe = describe
        self.pv = stats["pv"]
        self.max_pv = stats["pv"]
        self.attack = stats["attaque"]
        self.defense = stats["defense"]
        self.speed = stats["vitesse"]
        self.capacites = capacites if capacites else []

    def is_fainted(self):
        return self.pv <= 0

    def take_damage(self, damage):
        self.pv -= damage
        if self.pv < 0:
            self.pv = 0

    def __str__(self):
        return f"{self.name} ({self.type1}/{self.type2}) - {self.pv}/{self.max_pv} HP"
    
    def choose_move(self, is_player=True):
        if not self.capacites:
            print(f"{self.name} n'a aucune capacité disponible ! Utilisation de Charge par défaut.")
            return "Charge", 40

        if is_player:
            print(f"\nCapacités disponibles pour {self.name} :")
            for idx, cap in enumerate(self.capacites):
                print(f"{idx + 1}. {cap}")

            while True:
                try:
                    choice = int(input("Choisissez une capacité (numéro) : ")) - 1
                    if 0 <= choice < len(self.capacites):
                        selected = self.capacites[choice]
                        print(f"{self.name} utilise {selected.name} !")
                        return selected.name, selected.power
                    else:
                        print("Numéro invalide. Essayez encore.")
                except ValueError:
                    print("Entrée invalide. Entrez un numéro.")
        else:
            selected = random.choice(self.capacites)
            print(f"{self.name} utilise {selected.name} !")
            return selected.name, selected.power
    

