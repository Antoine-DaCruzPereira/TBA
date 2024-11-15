#player

class player:

    #define the constructor
    def __init__(self,name,team, inventaire):
        self.name = name
        self.team = team
        self.inventaire = inventaire
        self.current_region = None

    def move(self,direction):
        next_region = self.current_region.exit[direction]

        if next_region is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        

        self.current_room = next_region
        print(self.current_room.get_long_description())
        return True
    
    