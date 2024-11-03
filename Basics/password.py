# Import required modules to work

# open the password holding file
password_file = open("./secret_password.txt")

# Read the opened file
secret_password = password_file.read()

# Ask user to input the password
print("Please enter the password to verify!!")
typed_password = input()

# Check if password from file and user password are same or not
if typed_password == secret_password:
    print("Access Granted")
    if typed_password == "12345":
        print("That password is one an idiot puts on their luggage")
else:
    print("Access Denied.")
    exit()
