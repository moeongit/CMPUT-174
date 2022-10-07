alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(text, shift):
    decrypted = ""
    for letter in text:
        if letter in alphabet_lower:
            position = alphabet_lower.find(letter)
            new_letter = (position + shift) % 26
            new_character = alphabet_lower[new_letter]
            decrypted += new_character
        elif letter in alphabet_upper:
            position = alphabet_upper.find(letter)
            new_letter = (position + shift) % 26
            new_character = alphabet_upper[new_letter]
            decrypted += new_character
        else:
            decrypted += letter
    return decrypted

def main():
    text = input("Enter a text to decipher ")
    print(f"Your decrypted message is: {decrypt(text, -3)}")
main()