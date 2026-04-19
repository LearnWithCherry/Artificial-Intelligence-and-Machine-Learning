# Tuple immutable 
t = (1,2,3,4,5,4,4,4,4,4,4)
     

# t[2] = 100 not possible
 
# print(t[2])
# sum = 0
# for val in t:
#     print(val)
#     sum += val

# print(sum)

# tuple methoda

'''
t.index(value) return index of the value where it is appear for the first time 
t.count(value)
'''

print(t.index(4))
print(t.count(4))