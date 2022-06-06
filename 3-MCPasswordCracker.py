# PASSWORD CRACKER DEMO
# We have a file of the 1000 most common passwords that we will compare the password to
# The hashed password we are cracking is 2b58af6dddbd072ed27ffc86725d7d3a

# Load up an MD5 library
import hashlib

# Set the password we are trying to crack into a constant
# By convention, constants are named with all caps
# This password is a hashed hexadecimal equivalent of a string
PASSWORD_TO_CRACK = "2b58af6dddbd072ed27ffc86725d7d3a"

plain_text_password = 'password'

# Hash the password from the file
hashed_password = hashlib.md5(plain_text_password.encode()).hexdigest()
print("Password " + plain_text_password + " hex hash " + hashed_password)

# Compare the file password to the password we are trying to crack
if hashed_password == PASSWORD_TO_CRACK:
    # If we have cracked the password
    # print a success message including the cracked password
    # note that we want to print the plain text not the hash!
    print("The password is " + plain_text_password)
    password_found = True

else:
    print("The password is NOT " + plain_text_password)

