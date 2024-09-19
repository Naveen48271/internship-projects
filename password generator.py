import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
    # Define character pools based on user preferences
    char_pool = ''
    
    if include_uppercase:
        char_pool += string.ascii_uppercase  # Uppercase letters A-Z
    
    if include_lowercase:
        char_pool += string.ascii_lowercase  # Lowercase letters a-z
    
    if include_digits:
        char_pool += string.digits  # Digits 0-9
    
    if include_special_chars:
        char_pool += string.punctuation  # Special characters like !, @, #, $, etc.
    
    if not char_pool:
        raise ValueError("At least one character set should be selected!")
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

# Example Usage
password_length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Generate password
password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_special_chars)
print(f"Generated password: {password}")
