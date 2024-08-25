#!/usr/bin/env python
# coding: utf-8
import streamlit as st
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
    st.title("Random Password Generator")
    password_length = st.number_input("Enter desired password length:", min_value=1, value=8)
    generated_password = generate_random_password(password_length)
    # Display the generated password
    st.write(f"Generated password: {generated_password}")
if __name__ == "__main__":
    main()

