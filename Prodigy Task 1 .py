def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_value = shift if encrypt else -shift
            result += chr((ord(char) - base + shift_value) % 26 + base)
        else:
            result += char
    return result

plaintext = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(plaintext, shift, True)
print("Encrypted message:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, shift, False)
print("Decrypted message:", decrypted_text)
