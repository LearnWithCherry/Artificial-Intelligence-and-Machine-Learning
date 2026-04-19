favColor = input("Enter you Fav color: ").lower()

match favColor:
    case "green":
        print("green you user fav color")
    case "blue":
        print("blue you user fav color")
    case "red":
        print("red you user fav color")
    case "purple":
        print("purple you user fav color")
    case "black":
        print("black you user fav color")
    case _:
        print("Color not present")