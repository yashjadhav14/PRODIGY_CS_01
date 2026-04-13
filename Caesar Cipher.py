def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Check if character is a letter
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Keep special characters unchanged

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# ===== Main Program =====
print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

print("\nChoose Operation:")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1/2): ")

if choice == '1':
    encrypted_text = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted_text)

elif choice == '2':
    decrypted_text = decrypt(message, shift)
    print("\nDecrypted Message:", decrypted_text)

else:
    print("Invalid choice!")