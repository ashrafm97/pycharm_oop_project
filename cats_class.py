class Cat():

    #this init in overrides animal class init

    def __init__(self, name = 'Señor Meow'):
        self.__name = name
        self.breed = 'Tabby'
        self.pref_catnip = 'N.Z. Catnip'
        self.fav_food = 'Grilled Chicken'
        self.__age = 1
        self.claws = 'clipped claws'
       # no need for self, as refering to the init from the parent class
        super().__init__(name, 4)

    def voice(self, worker_name = " "):
        return "meow " + worker_name
    def drink(self, drink_of_choice = " "):
        return "I love to lap from my lovely bowl " + drink_of_choice
    def tail(self):
        return "straight up cos I am happy!"
    def sleep(self):
        return "purrr purrr"
    def knock_off(self):
        return "This vase would look good on the floor >:)"
    def age_getter(self):
        return self.__age
    def name_setter(self, name):
       self.__name = name
       return "New Name " + name
    