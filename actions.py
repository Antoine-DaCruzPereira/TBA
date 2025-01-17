import random
from room import Room
from config import DEBUG
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

CARAC_SUP ="nseoudrtpw"
CARAC_REPLACE = "NSEOUDRTPW"


class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        table = str.maketrans(CARAC_SUP, CARAC_REPLACE)
        direction = direction.translate(table)
        # Move the player in the direction specified by the parameter.
        if direction == "N":
            player.move(direction)
            return True
        elif direction == "NORD":
            direction = "N"
            player.move(direction)
            return True
        elif direction == "S":
            player.move(direction)
            return True
        elif direction == "SUD":
            direction = "S"
            player.move(direction)
            return True
        elif direction == "E":
            player.move(direction)
            return True
        elif direction == "EST":
            direction = "E"
            player.move(direction)
            return True
        elif direction == "EAST":
            direction = "E"
            player.move(direction)
            return True
        elif direction == "O":
            player.move(direction)
            return True
        elif direction == "OUEST":
            direction = "O"
            player.move(direction)
            return True
        elif direction == "WEST":
            direction = "O"
            player.move(direction)
            return True
        elif direction == "U":
            player.move(direction)
            return True
        elif direction == "UP":
            direction = "U"
            player.move(direction)
            return True
        elif direction == "D":
            player.move(direction)
            return True
        elif direction == "DOWN":
            direction = "D"
            player.move(direction)
            return True
        else:
            print("\nLa Direction n'est pas valide!\n")
            

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    def history(game, list_of_words, number_of_parameters):
        if number_of_parameters == 0:
            return(game.player.get_history())
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
    
    def back(game, list_of_words, number_of_parameters):
        if len(game.player.history) != 0:
            game.player.current_room = game.player.history.pop()
            print(game.player.current_room.get_long_description())
            game.player.get_history()
            return True
        else:
            print("\nImpossible de revenir en arrière, aucun déplacement enregistré.")
            return False
        
    def look(game, list_of_words, number_of_parameters):
        if number_of_parameters == 0:
            print("\n--- Contenu de la pièce ---")
            game.player.current_room.get_inventory()
            game.player.current_room.get_people()
            #return(game.player.current_room.get_inventory())
            return True
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
    
    def take(game, list_of_words, number_of_parameters):
        if number_of_parameters == 1:
            item = list_of_words[1]
            inventory = game.player.current_room.inventory
            if item in inventory:
                game.player.inventory[item] = inventory[item]
                del inventory[item]
                print(f"\nVous avez pris {item}.")
                return True
            else:
                print("\nCet item n'est pas dans la salle.")
                return False
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
    def drop(game, list_of_words, number_of_parameters):
        if number_of_parameters == 1:
            item = list_of_words[1]
            inventory = game.player.inventory
            if item in inventory:
                game.player.current_room.inventory[item] = inventory[item]
                del inventory[item]
                print(f"\nVous avez posé {item}.")
                return True
            else:
                print("\nCet item n'est pas dans votre inventaire.")
                return False
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
    def check(game, list_of_words, number_of_parameters):
        if number_of_parameters == 0:
            return(game.player.get_inventory())
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
    def use(game, list_of_words, number_of_parameters):
        item = list_of_words[1]
        if number_of_parameters == 1:
            if item in game.player.inventory:
                if item == "Beamer":
                    return(game.Beamer.use(game))
                else:
                    print("\nCet item ne peut pas charger.")
                    return False
            else:
                print("\nCet item n'est pas dans l'inventaire.")
                return False
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
    def charge(game, list_of_words, number_of_parameters):
        item = list_of_words[1]
        if number_of_parameters == 1:
            if item in game.player.inventory:
                if item == "Beamer":
                    return(game.Beamer.charge(game))
                else:
                    print("\nCet item ne peut pas charger.")
                    return False
            else:
                print("\nCet item n'est pas dans l'inventaire.")
                return False
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
    def talk(game, list_of_words, number_of_parameters):
        if len(list_of_words) < 2:
            print("\nUsage : talk <someone>")
            return False
        
        if number_of_parameters == 1:
            target_name = list_of_words[1]
            if DEBUG:
                print(f"DEBUG: Cible de la commande talk -> {target_name}")

            if target_name in game.player.current_room.people:
                NPC = game.player.current_room.people[target_name]
                NPC.get_msg()
                return True
            else:
                print(f"\nIl n'y a personne nommé {target_name} ici.")
                return False
        else:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
            
    def battle(game, list_of_words, number_of_parameters):
        if len(list_of_words) < 2:
            print("\nUsage : battle <someone>")
            return False

        target_name = list_of_words[1]
        if target_name in game.player.current_room.people:
            npc = game.player.current_room.people[target_name]
            npc.initiate_battle(game.player)
            return True
        else:
            print(f"\nIl n'y a personne nommé {target_name} ici.")
            return False
        

    def unlock(game, list_of_words, number_of_parameters):
        if number_of_parameters == 1:
            direction = list_of_words[1]
            table = str.maketrans(CARAC_SUP, CARAC_REPLACE)
            direction = direction.translate(table)
            current_room = game.player.current_room
            next_room = current_room.exits.get(direction)

            if isinstance(next_room, Room) and next_room.locked:
                for item in game.player.inventory.values():
                    if next_room.unlock(item):
                        return True
                print("Vous n'avez pas la clé appropriée.")
                return False
            else:
                print("Il n'y a pas de porte verrouillée dans cette direction.")
                return False
        else:
            print("Utilisation : unlock <direction>")
            return False