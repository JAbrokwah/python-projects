"""
Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25.
This cipher rotates the letters of the alphabet (A to Z).
The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A).
So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC".
This simple "monoalphabetic substitution cipher" provides almost no security,
because an attacker who has the encoded message can either use frequency analysis to guess the key,
or just try all 25 keys.
"""
from exceptions import InvalidKeyException, InvalidModeException

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def caesar_cipher(key, string, mode):
    """
    A Caesarean cipher is used on a string given the provided key.
    :param key: int in range [1, 25]
    :param string: string to encode/decode
    :param mode: selection of encryption (1) or decryption (2)
    """

    # validate input
    if type(key) != int:
        raise TypeError("Input param 'key' was not type of int")
    if type(mode) != int:
        raise TypeError("Input param 'mode' was not type of int")
    if type(string) != str:
        raise TypeError("Input param 'string' was not type of str")
    if key < 1 or key > 25:
        raise InvalidKeyException
    if string == "":
        return ""
    if mode < 1 or mode > 2:
        raise InvalidModeException

    # perform cipher
    result = ""
    string = string.upper()

    if mode == 1:
        for character in string:
            if str.isalpha(character):
                encrypted_char = encrypt(key, character)
                result += LETTERS[encrypted_char]
            else:
                result += character
    else:
        for character in string:
            if str.isalpha(character):
                decrypted_char = decrypt(key, character)
                result += LETTERS[decrypted_char]
            else:
                result += character

    return result


def encrypt(key, letter):
    return (LETTERS.index(letter) + key) % 26


def decrypt(key, letter):
    return (LETTERS.index(letter) - key) % 26
