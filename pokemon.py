#pokemon
import json


class pokemon:

    #define the constructor
    def __init__(self,name,type1,type2,describe,camp,stats):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.describe = describe
        self.camp = camp #camp define if it's a pokemon ally or enemy
        self.stats = stats
