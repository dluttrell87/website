global name


def hello():
    global name
    name = input("What is your name? ")
    return name


hello()
print("\n", "Hi", name)
