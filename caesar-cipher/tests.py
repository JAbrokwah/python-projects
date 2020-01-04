import unittest

from caesar_cipher import caesar_cipher
from exceptions import InvalidKeyException, InvalidModeException


class CaesarCipherTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual("", caesar_cipher(1, "", 1))

    def test_single_char_lower_enc(self):
        self.assertEqual("B", caesar_cipher(1, "a", 1))

    def test_single_char_upper_enc(self):
        self.assertEqual("B", caesar_cipher(1, "A", 1))

    def test_single_char_lower_dec(self):
        self.assertEqual("A", caesar_cipher(1, "b", 2))

    def test_single_char_upper_dec(self):
        self.assertEqual("A", caesar_cipher(1, "B", 2))

    def test_multi_char_lower_enc(self):
        self.assertEqual("BCD", caesar_cipher(1, "abc", 1))

    def test_multi_char_upper_enc(self):
        self.assertEqual("BCD", caesar_cipher(1, "ABC", 1))

    def test_multi_char_lower_dec(self):
        self.assertEqual("AB", caesar_cipher(1, "bc", 2))

    def test_multi_char_upper_dec(self):
        self.assertEqual("AB", caesar_cipher(1, "BC", 2))

    def test_multi_char_mixed_enc(self):
        self.assertEqual("BCD", caesar_cipher(1, "Abc", 1))

    def test_multi_char_mixed_dec(self):
        self.assertEqual("ABC", caesar_cipher(1, "bCD", 2))

    def test_invalid_key_exc(self):
        with self.assertRaises(InvalidKeyException):
            caesar_cipher(0, "a", 1)

    def test_invalid_mode_exc(self):
        with self.assertRaises(InvalidModeException):
            caesar_cipher(1, "a", 0)

    def test_invalid_key_type(self):
        with self.assertRaises(TypeError):
            caesar_cipher("1", "a", 1)
        with self.assertRaises(TypeError):
            caesar_cipher(bool, "a", 1)
        with self.assertRaises(TypeError):
            caesar_cipher(1.2, "a", 1)

    def test_invalid_mode_type(self):
        with self.assertRaises(TypeError):
            caesar_cipher(1, "a", "1")
        with self.assertRaises(TypeError):
            caesar_cipher(1, "a", False)
        with self.assertRaises(TypeError):
            caesar_cipher(1, "a", 32.3)


if __name__ == '__main__':
    unittest.main()
