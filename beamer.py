#Beamer
class Beamer:
        
    def __init__(self):
        self.charged_room = None

    def charge(self, room):
        self.charged_room = room
        print(f"Le beamer est chargé dans la pièce : {room.name}")

    def use(self, game):
        if self.charged_room:
            print(f"Vous utilisez le beamer et êtes téléporté dans : {self.charged_room.name}")
            game.player.current_room = self.charged_room
            self.charged_room = None
        else:
            print("Le beamer n'est pas chargé !")