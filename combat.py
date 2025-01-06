#combat
import math


class Combat:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def calculate_damage(self, attacker, defender, move_power):
        
        damage = ((move_power * (attacker.attack / defender.defense)) / 50) + 2
        return math.floor(damage)

    def turn(self, attacker, defender):
        
        move_name, move_power = attacker.choose_move()
        print(f"{attacker.name} utilise {move_name} !")

        damage = self.calculate_damage(attacker, defender, move_power)
        defender.take_damage(damage)
        print(f"{defender.name} subit {damage} points de dégâts !")

        if defender.is_fainted():
            print(f"{defender.name} est K.O. !")
            return True
        return False

    def start_battle(self):
        
        print(f"\nUn combat commence entre {self.trainer1.name} et {self.trainer2.name} !")

        while self.trainer1.has_available_pokemon() and self.trainer2.has_available_pokemon():
            pokemon1 = self.trainer1.choose_next_pokemon()
            pokemon2 = self.trainer2.choose_next_pokemon()

            print(f"\n{self.trainer1.name} envoie {pokemon1.name} !")
            print(f"{self.trainer2.name} envoie {pokemon2.name} !")

            
            while not pokemon1.is_fainted() and not pokemon2.is_fainted():
                
                if pokemon1.speed >= pokemon2.speed:
                    first, second = pokemon1, pokemon2
                else:
                    first, second = pokemon2, pokemon1

                
                if self.turn(first, second):
                    break

                
                if self.turn(second, first):
                    break

            print("\n---")

        
        if self.trainer1.has_available_pokemon():
            print(f"{self.trainer1.name} remporte le combat !")
        else:
            print(f"{self.trainer2.name} remporte le combat !")