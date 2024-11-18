# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        Prypiat = Room("Prypiat", "Dans la ville de Prypiat, c'est la ville où commence votre aventure, située aux abords de la zone d'exclusion de Tchernobyl ☢.")
        self.rooms.append(Prypiat)
        Route = Room("Route", "C'est la route sinistre, abandonnée qui relie Prypiat et la centrale de Tchernobyl.")
        self.rooms.append(Route)
        Périmètre_La_Centrale = Room("Périmètre de la centrale", "Périmètre d'exclusion radioactif autour de Tchernobyl, des pokemons corrompus par la radioactivitée dû à l'explosion ☢.")
        self.rooms.append(Périmètre_La_Centrale)
        Entrée_De_La_Centrale = Room("Entrée de la centrale", "En plein milieu de la zone d'exclusion, apparaît au milieu de la brume, deux grande porte donne accès à la centrale , vous appercevez une figure patrouillant dans la pièce.")
        self.rooms.append(Entrée_De_La_Centrale)
        Couloir_Est = Room("Couloir Est", "Couloir lugubre, avec des lumières clignotante, qui relie l'entrée, Salle des Machines 1, Salle du Personnels, Salle de Controle du réacteur n°1.")
        self.rooms.append(Couloir_Est)
        Couloir_Ouest = Room("Couloir Ouest", "Couloir lugubre, avec des lumières clignotante, qui relie l'entrée; Salles des Machines 1, Salle de Controle du réacteur n°2.")
        self.rooms.append(Couloir_Ouest)
        Salle_De_Controle_1 = Room("Salle de controle du Réacteur n°1","Salle de controle qui servait à piloter le réacteur n°1 avant la catastrophe.")
        self.rooms.append(Salle_De_Controle_1)
        Salle_De_Controle_2 = Room("Salle de controle du Réacteur n°2","Salle de controle qui servait à piloter le réacteur n°2 avant la catastrophe.")
        self.rooms.append(Salle_De_Controle_2)
        Salle_Du_Personnel = Room("Salle du personnel","Salle contenant du matériels servant à la maintenance de la centrale.")
        self.rooms.append(Salle_Du_Personnel)
        Réacteur_1 = Room("Réacteur n°1","Réacteur de la première tranche, le réacteur est délabré avec des barres de combustible visiblent depuis l'entrée du réacteur, il émet de la radioactivité en permanence depuis le jour de la catastrophe.")
        self.rooms.append(Réacteur_1)
        Réacteur_2 = Room("Réacteur n°2","Réacteur de la deuxième tranche, le réacteur a subi des dommages à la tuyauterie du premier circuit , il émet de la radioactivité en permanence depuis le jour de la catastrophe.")
        self.rooms.append(Réacteur_2)
        Réacteur_4 = Room("Réacteur n°4","Réacteur de la quatrième tranche, c'est l'épicentre de la catastrophe, le coeur du réacteur est à ciel ouvert, il émet de la matière radioactive en permanence depuis J=0.")
        self.rooms.append(Réacteur_4)
        Salle_Des_Machines_1 = Room("Salle des machines n°1"," Salle des machines de la première tranche, Elle est reliée par la tuyauterie du deuxième circuit au réacteur n°1, l'immense salle est anormalement silencieuse et radioactive.")
        self.rooms.append(Salle_Des_Machines_1)
        Salle_Des_Machines_2 = Room("Salle des machines n°2"," Salle des machines de la deuxoème tranche, Elle est reliée par la tuyauterie du deuxième circuit au réacteur n°2, l'immense salle est anormalement silencieuse et radioactive.")
        self.rooms.append(Salle_Des_Machines_2)

        # Create exits for rooms

        Prypiat.exits = {"N" : None, "E" : Route, "S" : None, "O" : None, "U":None, "D":None}
        Route.exits = {"N" : Périmètre_La_Centrale , "E" : None, "S" : None, "O" : None,"U":None, "D":None}
        Périmètre_La_Centrale.exits = {"N" : Entrée_De_La_Centrale, "E" : None, "S" : None, "O" : None,"U":None, "D":None}
        Entrée_De_La_Centrale.exits = {"N" : None, "E" : Couloir_Est, "S" : None, "O" : Couloir_Ouest,"U":Réacteur_4, "D":None}
        Couloir_Est.exits = {"N" : Salle_De_Controle_1, "E" : Salle_Du_Personnel, "S" : Salle_Des_Machines_1, "O" : Entrée_De_La_Centrale}
        Couloir_Ouest.exits = {"N" : Salle_De_Controle_2, "E" : Entrée_De_La_Centrale, "S" : Salle_De_Controle_2, "O" : None}
        Salle_De_Controle_1.exits={"N" : Réacteur_1, "E" : None, "S" : Couloir_Ouest ,"O" : None, "U":None, "D":None}
        Salle_De_Controle_2.exits={"N" : Réacteur_2, "E" : None, "S" : Couloir_Est ,"O" : None, "U":None, "D":None}
        Salle_Du_Personnel.exits = {"N" : None, "E" : None, "S" : None, "O" : Couloir_Est, "U":None, "D":None}
        Réacteur_1.exits = {"N" : None, "E" : None, "S" : Salle_De_Controle_1, "O" : None, "U":None, "D":None}
        Réacteur_2.exits = {"N" : None, "E" : None, "S" : Salle_De_Controle_2, "O" : None, "U":Réacteur_4, "D":None}
        Réacteur_4.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U":None, "D":Réacteur_2}
        Salle_Des_Machines_1.exits = {"N" : Couloir_Est, "E" : None, "S" : None, "O" : None, "U":None, "D":None}
        Salle_Des_Machines_2.exits = {"N" : Couloir_Ouest, "E" : None, "S" : None, "O" : None, "U":None, "D":None}


        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Prypiat

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word != "":
            if command_word not in self.commands.keys():
                print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
