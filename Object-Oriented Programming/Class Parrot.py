# create class
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
blu = Parrot("Blu" , 10)

print("Blu is a {}".format(blu.species))

print("{} is {} years old". format(blu.name, blu.age))
    