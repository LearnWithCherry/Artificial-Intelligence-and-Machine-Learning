# dict is immutable

d = {   1 : "one",
        2 : ["CAR","Money"],
        3 : 4.321,
        4 : "Rajat"
    }
d[3] = 5.236
d[5] = True

# print(d[])
# print(type(d))
dk = d.keys()
dv = d.values()
# print(d.keys())
# print(d.values())

# print("Printing value: ",dk)
# print("Printing value: ",dv)


# method

# d.keys()
# d.values()
# d.items()
# d.get(paramater)
# d.update(parameter)

# print(d.items())
print(d.get(4))

d.update({
    5:"Student"
})

print(d.items())