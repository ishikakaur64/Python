def calculate_tuple_product(numbers_tuple):
    product = 1
    
    for num in numbers_tuple:
        product *= num
        
    return product
given_tuple = (2, 4, 1, 5, 3) 

result = calculate_tuple_product(given_tuple)

print(f"The given tuple is: {given_tuple}")
print(f"The product of all numbers in the tuple is: {result}")