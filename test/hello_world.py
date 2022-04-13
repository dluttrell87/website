name = ""


def hello():
    # set as global
    global name
    name = input("What is your name? ")
    return name


hello()
print("\n", "Hi", name)