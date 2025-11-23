class Employee:

    def __init__(self):
        print('Employee created')

    def __del_(self):
        print("Destructor called")

def Create_obj():
    print('Making Object......')
    obj = Employee()
    print('function end......')
    return obj

print('Calling Create_obj() function.....')
obj = Create_obj()
del obj

        