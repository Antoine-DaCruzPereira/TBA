# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = dict()
        self.exits = {}
        self.people = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\n{self.description}\n\n{self.get_exit_string()}\n"


    def get_inventory(self):
        if len(self.inventory) != 0:
            for item in self.inventory:
                print("     - ",self.inventory.get(item).name)
            return True
        elif len(self.people) != 0:
            for name, item in self.people.items():
                print(f"    -{item}")
        else:
            print("\nIl n'y a rien ici.")
            return False
        
    def get_people(self):
        if len(self.people) > 0:
            print(f"Personnages présents dans {self.name} :")
            for person_name, person in self.people.items():
                print(f"  - {person_name}: {person.description}")
            return True
        else:
            print(f"Aucun personnage dans {self.name}.")
            return False