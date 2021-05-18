class Employee:
    pass

def local_variables():
    a = 10
    b = 20

e = Employee()
print(e.__class__.__name__)
print(local_variables.__code__.co_nlocals)