def decrypt_ceaser(text, shift):
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

def decrypt_atbash(str):
    decrypt = ""
    for letter in str:
        if 65 <= ord(letter) <= 90:
            newletter = chr(90 - (ord(letter) - 65))
            decrypt = decrypt + newletter
        elif 97 <= ord(letter) <= 122:
            newletter = chr(122 - (ord(letter) - 97))
            decrypt = decrypt + newletter
        else:
            decrypt = decrypt + letter
    return decrypt

def decrypt_a1z26(str):
    decrypt = ""

    if 1 <= int(letter) <= 26:
        number = 65 + int(letter) - 1
        letter = chr(number)
        decrypt = decrypt + letter
    else:
        decrypt = decrypt + letter
    return decrypt




def main():
    text = input("Enter a string: ")
    print("Let's try all the methods we have:")
    print(f"Ceaser cipher: {decrypt_ceaser(text, -3)}")
    print(f"Atbash cipher: {decrypt_atbash(text)}")
    print(f"A1Z26 cipher: {decrypt_a1z26(text)}")
main()



