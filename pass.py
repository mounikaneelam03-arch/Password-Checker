import re

password = input("Enter your password: ")

# Conditions using regex
length_check = len(password) >= 8
upper_check = re.search(r"[A-Z]", password)
number_check = re.search(r"[0-9]", password)
special_check = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

if length_check and upper_check and number_check and special_check:
    print("Strong Password 💪")
else:
    print("Weak Password ❌")