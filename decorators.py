# In python, functions itself are values
# Hence we can treat functions as arguments for other functions, i.e Decorators

# Decorator
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

# Adding a decorator to a function
@announce
def hello():
    print("Hello, world!")

hello()
