class myClass:

    __privateVar = 27;

    def __privMeth(self):
        print("I'm inside class")

    def hello(self):
        print("Private Variable value: ",myclass._privateVar)


Zoo = myclass()
Zoo.hello()
Zoo.__privMeth