# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = dict()
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        self.history.append(self.current_room)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        if len(self.history) != 0:
            for room in self.history:
                print("     - ",room.name)
            return True
        else:
            print("\nAucun historique disponible.")
            return False
        
    def get_inventory(self):
        if len(self.inventory) != 0:
            for item in self.inventory:
                print("     - ",item.name)
            return True
        else:
            print("\nVotre inventaire est vide.")
            return False
        
    