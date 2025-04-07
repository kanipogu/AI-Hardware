def encrypt(plaintext, shift):
    """Encrypt the plaintext using Caesar cipher."""
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Handle both uppercase and lowercase letters
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += shifted_char
        else:
            # If it's not a letter, don't change it (punctuation, spaces, etc.)
            ciphertext += char
    
    return ciphertext


def decrypt(ciphertext, shift):
    """Decrypt the ciphertext using Caesar cipher."""
    return encrypt(ciphertext, -shift)  # Decrypting is just reversing the shift


if __name__ == "__main__":
    text = "Hello, World!"  # Example text
    shift = 3  # Shift for the cipher
    
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted: {decrypted_text}")
