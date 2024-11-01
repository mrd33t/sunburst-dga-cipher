#!/usr/bin/env python3

# Example usage of SUNBURST DGA Cipher
from sunburst_dga_cipher import sunburst_encode, sunburst_decode

# Example 1: Basic encoding
original_text = "hello friends"
encoded = sunburst_encode(original_text)
print(f"Original: {original_text}")
print(f"Encoded: {encoded}")

# Example 2: Basic decoding
decoded = sunburst_decode(encoded)
print(f"Decoded: {decoded}")

# Example 3: Multiple word encoding
message = "this is a secret message"
encoded_message = sunburst_encode(message)
print(f"\nOriginal message: {message}")
print(f"Encoded message: {encoded_message}")
