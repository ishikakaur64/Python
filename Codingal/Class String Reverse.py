class StringReverse:
    def _init_(self, text):
        self.__text = text   # private variable

    def reverse(self):
        words = self.__text.split()
        result = ""
        for w in words:
            result += w[::-1] + " "
        return result.strip()


obj = StringReverse("Python is easy")
print(obj.reverse())