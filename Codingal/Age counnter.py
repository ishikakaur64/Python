# Age Counter using Exception Handling

try:
    age = int(input("Enter your age: "))

    if age % 2 == 0:
        print("The age is even.")
    else:
        print("The age is odd.")

except NameError:
    print("NameError: You are using a variable that is not defined.")

except ValueError:
    print("ValueError: Please enter numbers only for age.")

except:
    print("Some error occurred.")