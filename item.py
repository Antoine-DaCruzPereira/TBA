#Item

class item:


    # The constructor.
    def __init__(self,name,description,weight,key_id=None):
        self.name = name
        self.description = description
        self.weight = weight
        self.key_id = key_id

    def is_key(self):
        return self.key_id is not None

    def __str__(self):
        return f"{self.command_word} : {self.help_string} ({self.weight} kg)"
    