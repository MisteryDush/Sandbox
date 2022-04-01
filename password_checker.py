print("Password must longer than 4 and shorter than 8")
password = input("Enter the password: ")
while len(password) > 8 or len(password) < 4:
    print("Password doesnt meet requirements ")
    password = input("Enter the password: ")
print("*"*len(password))

