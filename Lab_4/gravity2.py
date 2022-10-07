def decrypt_ceaser(text, shift): # Parameters are text and shift
    decrypt = "" # Made a string for the decrypt message
    for letter in text:
        if 65 <= ord(letter) <= 90: # used ord and ascii values for A-Z
            newletter = chr(65 + (ord(letter)-65+shift) % 26) # Used math to shift the letter to the left by 3
            decrypt = decrypt + newletter
        elif 97 <= ord(letter) <= 122: # Did the same for lowercase letters
            newletter = chr(97 + (ord(letter)-97+shift) % 26)
            decrypt = decrypt + newletter
        else:
            decrypt = decrypt + letter
    return decrypt

def decrypt_atbash(str): # Parameter is string
    decrypt = ""
    for letter in str:
        if 65 <= ord(letter) <= 90: # Used ord and Ascii values to implement this
            newletter = chr(90 - (ord(letter) - 65)) # 90 (Z) is added to the ascii value of the inputted letter and subtracted by 65
            decrypt = decrypt + newletter
        elif 97 <= ord(letter) <= 122:
            newletter = chr(122 - (ord(letter) - 97))
            decrypt = decrypt + newletter
        else:
            decrypt = decrypt + letter
    return decrypt

def decrypt_A1Z26(str):
    decrypt = ""
    dash = str.find('-')
    while True:
        if dash == -1:
            letter = str
        else:
            letter = str[0:dash]
            str = str[dash+1:]
        if letter == "":
            break
        count = 0
        if " " in letter:
            for counting in letter:
                if counting != ' ':
                    count+=1
                else:
                    break
        if count == 0:
            decrypt += chr(65 + (int(letter) -1))
        else:
            letter_1 =int(letter[0:count])
            decrypt += chr(65 + (int(letter_1) -1))
            letter_2 = ' '
            decrypt += letter_2
            letter_3 = int(letter[count+1:])
            decrypt += chr(65 + (int(letter_3) -1))
        #print(decrypt)
        if dash == -1:
            break
        dash = str.find('-')
    return decrypt    



def main():
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")
    print(f"Ceaser cipher: {decrypt_ceaser(text, -3)}")
    print(f"Atbash cipher: {decrypt_atbash(text)}")
    print(f"A1Z26 cipher: {decrypt_A1Z26(text)}")
main()
