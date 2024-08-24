def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

# Get user input
message = input("Enter your message: ")
shift = int(input("Enter shift value (0-25): "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = caesar_cipher(encrypted_message, -shift)
print("Decrypted message:", decrypted_message)