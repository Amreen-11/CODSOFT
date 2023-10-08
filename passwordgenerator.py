import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
  length = int(input("Enter the password length: "))
  if length < 8:
    print("Password length should be at least 8 characters.")
  else:
    password = generate_password(length)
    print("Generated Password: ", password)
    
if __name__ == "__main__":
    main()
