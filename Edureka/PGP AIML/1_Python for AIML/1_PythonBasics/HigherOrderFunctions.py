def test(function):
    def text_lower(arg):
        print(arg.lower())
        function(arg)
        return arg.lower()
    return text_lower

@test
def square(x):
    print(x)
    return x

def max_square(fn, x):
    return fn(x)

def double_max_square(fn, x):
    return fn(fn(x), x)



square("THIS")
print(bool(-1))
