from string import ascii_uppercase

ALPHABET = list(ascii_uppercase)

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        alphabet_len = len(self.alphabet)
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                letter_cipher = (letter_index + key) % alphabet_len
                encrypted_text.append(self.alphabet[letter_cipher])
            else:
                encrypted_text.append(letter)  # Giữ nguyên ký tự không có trong bảng chữ cái
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        alphabet_len = len(self.alphabet)
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                letter_cipher = (letter_index - key) % alphabet_len
                decrypted_text.append(self.alphabet[letter_cipher])
            else:
                decrypted_text.append(letter)  # Giữ nguyên ký tự không có trong bảng chữ cái
        return ''.join(decrypted_text)
