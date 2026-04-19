# sets collection of unique elements (immutable, unordered)

s = {1,2,2,3,3}
# print(s)
# print(s)

# print(type(s))

# print(len(s))

empty_set = set() # to create an empty set
# methods
s.add(4) 
s.remove(1)
s.pop()

# s.clear()
# print(s)



s1 = {1,2,3,4}
s2 = {4,5,6,7}

print(s1.union(s2)) # to print all the unique values 
print(s1.intersection(s2)) # to print only unique values
