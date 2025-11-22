class Dog:

    animal = "Dog"

    def _init_(self, breed, age):
        self.breed = breed
        self.age = age


dog1 = Dog("Labrador", 5)
dog2 = Dog("German Shepherd", 3)

print("Dog 1:", dog1.animal, dog1.breed, dog1.age)
print("Dog 2:", dog2.animal, dog2.breed, dog2.age)