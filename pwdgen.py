import random
import time
class PasswordGenerator:
    def __init__(self):
        self.uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.numbers = '0123456789'
        
    def generate_password(self, length):
        password = ''
        
        for _ in range(length):
            choice_list = random.choice([self.uppercase_letters, self.lowercase_letters, self.numbers])
            password += random.choice(choice_list)
        
        return password

# Create an instance of PasswordGenerator
password_generator = PasswordGenerator()

password_length = int(input("Enter the desired password length: "))
password = password_generator.generate_password(password_length)
print("Generated password:", password)
print('you have 7 seconds to copy it, COPY IT!')
time.sleep(7)
