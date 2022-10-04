alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt_ceaser(text, shift) :
    decrypt = ""
    for letter in text:
        if 65 <= ord(letter) <= 90:
            newletter = chr(65 + (ord(letter)-65+shift) % 26)
            decrypt = decrypt + newletter
        elif 97 <= ord(letter) <= 122:
            newletter = chr(97 + (ord(letter)-97+shift) % 26)
            decrypt = decrypt + newletter
        else:
            decrypt = decrypt + letter
    return decrypt



def main():
    user = input("Enter a string: ")
    print(decrypt_ceaser(user, -3))

main()



