#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string

def generate_random_password(length):
    # Combine all character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Initialize an empty password
    password = ""

    # Generate random characters as per the input length
    for _ in range(length):
        char_type = random.choice(all_characters)
        password += random.choice(char_type)

    return password

def main():
    try:
        password_length = int(input("Enter desired password length: "))
        if password_length <= 0:
            print("Please enter a positive integer for password length.")
            return

        generated_password = generate_random_password(password_length)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()

