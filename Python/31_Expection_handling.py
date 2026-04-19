def solving():
    print("")
    try:
        x = int(input("Enter a number: "))
        solve = 10/x

    except ZeroDivisionError:
        print(f"Dividing with Zero is not allowed")
    except ValueError:
        print(f"Entering String instead of Integer is not allowed")


    else:
        print(f"answer = {solve}")

    finally:
        print("Code is Running Properly.....")

    square = []

    for i in range (6):
        square.append(i*i)

    print(square)

# list Comprehensions



sq = [i*i for i in range(6) if i % 2 != 0]
print(sq)

words = ["Hello", "Python", "ai"]

words = [val.upper() for val in words]
print(words)