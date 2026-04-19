username = input("Enter Username: ")
password = input("Enter passowrd: ")

if(username == "1002" and password == "7410"):
    print("Success.")
else:
    if(username != "1002"):
        print("User name is Incorrect")
    else:
        print("Pass word is Incorrect")