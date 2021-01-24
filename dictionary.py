# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]

# print(plakalar[sehirler.index("kocaeli")])

# plakalar = {"key" : "value"}

# plakalar = { "kocaeli" : 41, "istanbul": 34}

# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6
# plakalar["kocaeli"] = "new value"

# print(plakalar)

users = {
    "gurkanaltunok": {
        "age": 18,
        "roles" : ["admin","user"],
        "email": "oguzgurkan2001@gmail.com",
        "address": "çorlu",
        "phone": "123456"
    },
        "oguzaltunok" : {
            "age" : 2,
            "roles":["user"]
        }

    
}

print(users["gurkanaltunok"]["age"])
print(users["gurkanaltunok"]["email"])
print(users["gurkanaltunok"]["address"])
print(users["oguzaltunok"]["age"])
# print(users["gurkanaltunok"]["roles"])
print(users["gurkanaltunok"]["roles"][0])



