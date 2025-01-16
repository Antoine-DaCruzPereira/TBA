#combat
import math
import random

class Combat:
    def __init__(self, trainer1, trainer2, game):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.game = game

    def calculate_damage(self, attacker, defender, move_power):
        damage = ((move_power * (attacker.attack / defender.defense)) / 50) + 2
        return math.floor(damage)

    def turn(self, attacker, defender, is_player_attacker=True):
        move_name, move_power = attacker.choose_move(is_player=is_player_attacker)
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
                    first_is_player = True
                else:
                    first, second = pokemon2, pokemon1
                    first_is_player = False

                if self.turn(first, second, is_player_attacker=first_is_player):
                    break

                if self.turn(second, first, is_player_attacker=not first_is_player):
                    break

            print("\n---")

        if not self.trainer1.has_available_pokemon():
            print("Game Over. Vous avez perdu le combat.")
            self.game.finished = True
        elif not self.trainer2.has_available_pokemon() and self.trainer2.name == "Urayne":
            print("Félicitations, vous avez gagné !")
            self.game.finished = True
        else:
            print(f"{self.trainer1.name} remporte le combat !")
            print("\nSorties disponibles dans cette pièce :")
            print(self.trainer1.current_room.get_exit_string())

