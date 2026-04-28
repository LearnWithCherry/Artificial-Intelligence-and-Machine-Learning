# Python program demonstrating all types of loops

# 1. FOR LOOP
print("---- FOR LOOP ----")
for i in range(1, 6):
    print("For Loop i =", i)


# 2. WHILE LOOP
print("\n---- WHILE LOOP ----")
j = 1
while j <= 5:
    print("While Loop j =", j)
    j += 1


# 3. BREAK STATEMENT
print("\n---- BREAK EXAMPLE ----")
for k in range(10):
    if k == 5:
        print("Breaking at k =", k)
        break
    print(k)


# 4. CONTINUE STATEMENT
print("\n---- CONTINUE EXAMPLE ----")
for m in range(5):
    if m == 2:
        continue
    print(m)


# 5. NESTED LOOP
print("\n---- NESTED LOOP ----")
for x in range(3):
    for y in range(3):
        print("x =", x, "y =", y)


# 6. LOOP WITH ELSE
print("\n---- LOOP WITH ELSE ----")
for z in range(3):
    print(z)
else:
    print("Loop finished successfully")


# 7. REAL USE CASE (SUM OF LIST)
print("\n---- SUM OF LIST ----")
numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print("Total =", total)
