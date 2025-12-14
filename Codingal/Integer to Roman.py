class Roman:
    def __init__(self, num):
        self.num = num

    def convert(self):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        roman = ""
        i = 0

        while self.num > 0:
            for _ in range(self.num // values[i]):
                roman += symbols[i]
                self.num -= values[i]
            i += 1

        return roman

number = int(input("Enter an integer: "))
obj = Roman(number)
print("Roman Numeral:", obj.convert())