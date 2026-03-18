import random
import string

print("---- One time password generator----")

length = int(input("Enter your password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print(f" Generator Password: {password}")


# password only number

"""def gen_num_password(length = 6):
    digits = "0123456789"
    password_num = ""
    for pw in range(length):
        password_num += random.choice(digits)
    return password_num

print("Number password: ", gen_num_password())"""