class InvalidKeyException(Exception):
    def __init__(self):
        Exception.__init__(self, "The Caesarean key must be in the range: [1, 25].")


class InvalidModeException(Exception):
    def __init__(self):
        Exception.__init__(self, "The mode selected must be:"
                                 "\n1 - Encryption"
                                 "\n2 - Decryption")
