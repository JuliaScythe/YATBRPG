class Player:
    def __init__(self, playerClass, name):
        self.initClass(playerClass)
        self.name = name

    def initClass(self, playerClass):
        #
        #   initClass(playerClass)
        #   Initializes all variables to be set to their respective class defaults
        #
        self.health = playerClass.health
        self.energy = playerClass.energy

        if playerClass.mana != 0:
            self.mana = playerClass.mana
        else:
            self.mana = 0

        self.inv = playerClass.defaultInv

        self.maxHealth = self.health
        self.maxEnergy = self.energy
        self.maxMana = self.mana
        
