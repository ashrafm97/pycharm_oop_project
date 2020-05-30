class Cat():

    def __init__(self, name = 'Señor Meow'):
        self.name = name
        self.breed = 'Tabby'
        self.pref_catnip = 'N.Z. Catnip'
        self.fav_food = 'Grilled Chicken'
        self.age = 1
        self.claws = 'clipped claws'

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
