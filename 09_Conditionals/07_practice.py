username = input("Enter username: ")
password = input("Enter password: ")
if (username=="admin" and password=="admin123"):
    print("Login successful")
elif (username!="admin" and password =="admin123"):
    print("Invalid username\nTry again later")
elif (password!="admin123" and username=="admin"):
    print("Invalid password\nTry again later")

else:
    print("something went wrong\nTry again later")