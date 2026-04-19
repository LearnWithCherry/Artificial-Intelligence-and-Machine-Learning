a = "Python"
b = "Language"
# print(len(a))

print(a + " " + b)

# print(a[2]) 

# for ch in a:
#     print(ch, end=" ")

# print(a[2:])
# print(a[-5:-1])
# print(a[:])

a = 5
b = 10

sum = a + b
print(f"Sum of a + b is {sum}")

# index based formatting

print("Sum of {1} and {0} is {2}".format(a,b,sum))
print("Sum of {0} and {1} is {2}".format(a,b,sum))

# value based formating

print("Values of var {a} & {b}".format(a = 10,b = 5))
