# PASSWORD CRACKER DEMO
# We have a file of the 1000 most common passwords that we will compare the password to
# The hashed password we are cracking is 2b58af6dddbd072ed27ffc86725d7d3a

# Load up an MD5 library
import hashlib

plain_text_password = 'password'

# Hash the password from the file
hashed_password = hashlib.md5(plain_text_password.encode()).hexdigest()
print("Password " + plain_text_password + " hex hash " + hashed_password)
