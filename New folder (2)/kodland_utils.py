import random

character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Masukkan panjang password"))
password = ""

for i in range(password_length):
    password += random.choice(character)
    
print(password)