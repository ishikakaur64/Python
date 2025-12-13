class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area:", 3.14 * self.r * self.r)

    def perimeter(self):
        print("Perimeter:", 2 * 3.14 * self.r)


c = Circle(5)
c.area()
c.perimeter()