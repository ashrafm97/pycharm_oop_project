# we import the classes here and initialize the objectives and run 'methods'
# this seperation will make the code more organized and help to seperate concers


from dogs_class import *

# initialise a dog object, by making a variable.... instances are happenings of things, so here its a 'breed' of Object

max_dog_instance = Dog()

# call the method .bark() on the object

print(max_dog_instance.bark("cat"))
print(max_dog_instance.eat())
print(max_dog_instance.fetch())
print(max_dog_instance.tail())
print(max_dog_instance.sleep())

print("walking Max home")

print(max_dog_instance.sleep())
print(max_dog_instance.eat())

#max saw the postman..... he is very concerned!

print(max_dog_instance.bark("LETTER MAN ! >:) "))


ringo_dog_instance = Dog("Ringo")
print(ringo_dog_instance)
