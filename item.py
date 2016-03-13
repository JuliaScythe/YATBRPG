# pickle serializes objects, enabling saving
import pickle
import itemtypes

class Item:
    def __init__(self, name, desc, itemType):
        self.name = name
        self.desc = desc
        self.itemType = itemType
