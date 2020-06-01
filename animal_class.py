class Animal():

    def __init__(self, name, species_argument, limbs):
        self.species_parameter = species_argument
        self.limbs = limbs
        self.name = name

#init in animal class overriden by the one in cats class

    def eat(self, food):
        return 'NOM, NOM, NOM! *tasty*'.lower()

    def sleep(self):
        return 'zzzz'
    def potty(self):
        return "relief!"
    def reproduce(self, partner ='... sorry, you are alone for now!'):
        return f"offspring of {self} and{partner}"

