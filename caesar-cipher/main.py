from caesar_cipher import caesar_cipher
from exceptions import InvalidKeyException, InvalidModeException

if __name__ == "__main__":
    print("Welcome to the Caesar Cipher!")

    string = input("Please enter the string to encode/decode: ")
    key = input("Please enter the key to encode/decode with: ")
    mode = input("Please select 1 for encryption, or 2 for decryption: ")

    try:
        cipher = caesar_cipher(int(key), string, int(mode))
        # output info to user
        print("Your ciphered string is: {}".format(cipher))
    except (InvalidKeyException, InvalidModeException) as error:
        print(error.args[0])
