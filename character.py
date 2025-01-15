#character
import random
from player import Player
from config import DEBUG
from combat import Combat

class Character(Player):

    def __init__(self,name,description,msgs,current_room,can_move=False):
        super().__init__(name,current_room)
        self.description = description
        self.msgs = msgs
        self.can_move = can_move

    def __str__(self):
        return f"{self.name} : {self.description}"
    
    def move(self):

        if not self.can_move:
            if DEBUG:
                print(f"DEBUG: {self.name} ne peut pas se déplacer.")
            return False

        if random.choice([True, False]):
            available_exits = list(self.current_room.exits.values())
            if not available_exits:
                if DEBUG:
                    print(f"DEBUG: {self.name} n'a aucune sortie disponible dans {self.current_room.name}.")
                return False

            next_room = random.choice(available_exits)
            if DEBUG:
                print(f"DEBUG: {self.name} se déplace de {self.current_room.name} à {next_room.name}.")

            del self.current_room.people[self.name]
            self.current_room = next_room
            self.current_room.people[self.name] = self
            return True
        else:
            if DEBUG:
                print(f"DEBUG: {self.name} reste dans {self.current_room.name}.")
            return False

    def get_msg(self):
        if not self.msgs:
            print(f"{self.name} n'a rien à dire.")
            return
        msg = self.msgs.pop(0)
        print(f"{self.name} dit : \"{msg}\"")
        self.msgs.append(msg)

    def initiate_battle(self, player):
        print(f"\n{self.name} vous défie en combat Pokémon !")
        battle = Combat(player, self)
        battle.start_battle()