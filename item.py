#Item

class item:


    # The constructor.
    def __init__(self,name,description,weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.command_word} : {self.help_string} ({self.weight} kg)"
    