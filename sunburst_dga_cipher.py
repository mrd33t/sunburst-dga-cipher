#!/usr/bin/env python3

# SUNBURST DGA Cipher Script

# Define the alphabets
pt_alphabet = "rq3gsalt6u1iyfzop572d49bnx8cvmkewhj"
ct_alphabet = "salt6u1iyfzop572d49bnx8cvmkewhjrq3g"

# Create translation tables
encode_trans = str.maketrans(pt_alphabet, ct_alphabet)
decode_trans = str.maketrans(ct_alphabet, pt_alphabet)

def sunburst_encode(text):
    return text.translate(encode_trans)

def sunburst_decode(text):
    return text.translate(decode_trans)

# Function to get user input and process
def process_input():
    while True:
        choice = input("Would you like to encode or decode? (e/d): ").lower()
        if choice in ['e', 'd']:
            break
        print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")

    text = input("Enter the text: ")

    if choice == 'e':
        result = sunburst_encode(text)
        print(f"Encoded message: {result}")
    else:
        result = sunburst_decode(text)
        print(f"Decoded message: {result}")

# Test the functions
print("Testing encoder and decoder:")
print(f"'hello friends' encodes to: {sunburst_encode('hello friends')}")
print(f"'n2huov' decodes to: {sunburst_decode('n2huov')}")

print("\nDecoding the given ciphertext:")
ciphertext = 'i3r eu116 usr e2hovt 5s2h ov6onr i3r 32f6r'
decoded_message = sunburst_decode(ciphertext)
print(f"Decoded message: {decoded_message}")

# Run the interactive part
print("\nInteractive SUNBURST DGA Cipher:")
process_input()
