#Beamer

class Beamer():
        
    def __init__(self):
        self.charged_room = None

    def charge(self):
        self.charged_room = self.player.current_room
        print(f"Le beamer est chargé dans la pièce : {self.player.current_room.name}")
        return True

    def use(self):
        if self.charged_room != None:
            print(f"Vous utilisez le beamer et êtes téléporté dans : {self.charged_room.name}\n")
            print(self.player.current_room.get_exit_string())
            self.player.current_room = self.charged_room
            self.charged_room = None
            return True
        else:
            print("Le beamer n'est pas chargé !")
            return False