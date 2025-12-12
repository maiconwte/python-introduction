def my_decorator(func):
    def wrapper(name):
        print(f"With, {name}")
        func(name)
        print(f"Goodbye, {name}")
    return wrapper

@my_decorator
def say_hello_classmethod(name):
    print(f"Hello, {name}")

say_hello_classmethod("John")

class MyClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(f"Before")
        self.func()
        print(f"After")

@MyClassDecorator
def with_decorator():
    print('Second function')

with_decorator()