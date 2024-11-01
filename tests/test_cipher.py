#!/usr/bin/env python3

import unittest
from sunburst_dga_cipher import sunburst_encode, sunburst_decode

class TestSunburstCipher(unittest.TestCase):
    def test_encoding(self):
        self.assertEqual(sunburst_encode("hello"), "n2huov")
        
    def test_decoding(self):
        self.assertEqual(sunburst_decode("n2huov"), "hello")
        
    def test_roundtrip(self):
        original = "hello friends"
        encoded = sunburst_encode(original)
        decoded = sunburst_decode(encoded)
        self.assertEqual(original, decoded)

if __name__ == '__main__':
    unittest.main()
