# x = "global x"

# def function():
#     x = "local x"

# function()
# print(x)

name = "Gürkan"

def changeName(new_name):
    name = new_name
    print(name)

changeName("Oğuz")

print(name)

########################

name = "global string"

def greeting():
    name = "Gürkan"

    def hello():
        name = ""
        print("Hello "+ name)

    hello()

greeting()

