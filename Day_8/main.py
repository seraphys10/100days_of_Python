from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    for c in text:
        if c not in alphabet:
            break
        for i in range(len(alphabet)):
            if c == alphabet[i]:
                while i + shift >= 26:
                    shift -= 26
                cipher_text += alphabet[i + shift]
                break
    print(cipher_text)
    return cipher_text

def decrypt(text, shift):
    plain_text = ""
    for c in text:
        for i in range(len(alphabet)):
            if c == alphabet[i]:
                while i - shift < 0:
                    shift += 26
                plain_text += alphabet[i - shift]
                break
    print(plain_text)
    return plain_text

def caeser(text, shift, direction):
    new_text = ""
    for c in text:
        for i in range(len(alphabet)):
            if c == alphabet[i]:
                if direction == 'encode':
                    while i + shift >= 26:
                        shift -= 26
                    new_text += alphabet[i + shift]
                    break
                elif direction == 'decode':
                    while i - shift < 0:
                        shift += 26
                    new_text += alphabet[i - shift]
                    break
    print(new_text)
caeser(text, shift, direction)