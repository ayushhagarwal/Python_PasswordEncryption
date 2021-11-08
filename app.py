from flask import Flask, bcrypt

# salt = b'$2b$12$Kh7S5S9FHT.WhzBa8tLZvO'
salt = bcrypt.gensalt()

password = "youareSmart123"
print(password)

password = bcrypt.hashpw(password.encode('utf-8'), salt)
print(password)
