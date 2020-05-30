# abstract and create the class dog

# class Dog():
#     pass


#initializing a Dog object
# dog_instance1 = Dog()


#print the Dog object
# print(dog_instance1)

# print(type(dog_instance1))


# you want to define classes on one side and run them on the other... you need to chop this code and place it in the run file


class Dog():

    #adding init 'method'... after everything
    #it comes defined but we can redefine it
    # this method stands for initializing class object - aka 'constructor' in other languages
    # allows us to set attributes to our dog objects
    # like the poor thing isnt even named lol
    # we should name it right?


    #self refers to the 'instance' of the 'object'


    def __init__(self, name = 'Mad Max'):
        self.name = name
        self.age = 7
        self.paws = 4
        self.fur = 'black and grey'
        self.fav_food = 'Steak'
# setting attributes 'name' to 'instances' of the Dog class... 'name is hardcoded now to be Max'


# this is a 'method' that can be used by the 'instance' Dog
    def voice(self, creature = " "):
        return 'woof, woof! I see you, damn ' + creature
# polymorphism, by default creature is nothing

    def eat(self):
        return 'nom, nom, NOM'.lower()

    def fetch(self):
        return 'zoom zoom'

    def tail(self):
        return 'wagging'
    def sleep(self):
        return 'zzzzZZZZzzz *drool* '

# in this file, you define the class dog and add attributes and method to the class, like fur or eyes or no. of legs etc etc. so no print statements...
# print("Filipe is a cool guy, as is Shahrukh")