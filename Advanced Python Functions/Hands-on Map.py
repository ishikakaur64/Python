#using map 
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n*n
square = list(map(sq, nums))
print(square)