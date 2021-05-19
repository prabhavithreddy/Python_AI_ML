def to_upper(fn):
    def inner(text):
        upper = text.upper()
        fn(upper)
    return inner

def get_string():
    return input("Enter a string")

@to_upper
def print_string(text):
    print("\n"+text)

print_string(get_string())