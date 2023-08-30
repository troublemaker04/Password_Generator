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

if len(password) > 50:
    with open('generatedpwd.txt','w')as file:
        file.write(password)
        print('since ur password was more than 50 charecters long, it was probably to big to fit on one screen, so we just saved it to a file! The file should be called, generatedpwd.')
        print('exiting in 8 seconds.')
        time.sleep(8)
        
else:
    print("Generated password:", password)
    print('you have 7 seconds to copy it, COPY IT!')
