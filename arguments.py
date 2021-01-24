# def changeName(n):
#     n = "Gürkan"

# name = "Oğuz"

# changeName(name)
# print(name)

# def change(n):
#     n[0] = "İstanbul"

# sehirler = ["Ankara", "İzmir"]

# change(sehirler[:])

# print(sehirler)

# def add(*params):
#     print(params[2])
#     return sum((params))

# def add(*params):
#     sum = 0

#     for n in params:
#         sum = sum+n

#     return sum


# print(add(10,20,30))
# print(add(10,20))
# print(add(10,20,30,40,50,60,70))

def displayUser(**params):
    for key, value in params.items():
        print("{} is {}".format(key,value))

displayUser(name= "Gürkan", age = 19, city = "İstanbul")
displayUser(name= "Oğuz", age = 25, city = "Florida", phone = "5421231212")
displayUser(name= "Altunok", age = 12, city = "Ankara", email= "oguzgurkan2001@gmail.com")

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10, 20, 30,40, 50, key1 = "value 10", key2 = "value 2")