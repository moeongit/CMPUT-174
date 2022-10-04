def decrypt_ceaser(text, shift):
    decrypt_ceas = ""
    for letter in text:
        if 65 <= ord(letter) <= 90:
            newletter = chr(65 + (ord(letter)-65+shift)%26)
            decrypt_ceas = decrypt_ceas + newletter
        elif 97 <= ord(letter) <= 122:
            newletter = chr(97 + (ord(letter)-97+shift)%26)
            decrypt_ceas = decrypt_ceas + newletter
        else:
            decrypt_ceas = decrypt_ceas + letter
    return decrypt_ceas
def decrypt_atbash(text): 

    decrypt_bash = ""
    for letter in text:
        ascii = ord(letter)
        if ascii>= 65 and ascii <=90:
            position = ascii - 65
            new_position = 25 - position
            new_ascii = new_position + 65
            new_letter = chr(new_ascii)
        else:
            new_letter = letter
            decrypt_bash = decrypt_bash + new_letter
        return decrypt_bash




def main():
    user = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:") 
    print(f"Ceaser cipher: {decrypt_ceaser(user, -3)}")
    print(f"Atbash cipher: {decrypt_atbash(user)}")
main()
