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

def decrypt_atbash(text): # Parameter is text
    decrypt = "" # Made a string for the decrypt message
    for letter in text:
        if 65 <= ord(letter) <= 90: # Used ord and Ascii values to implement this
            newletter = chr(90 - (ord(letter) - 65)) # 90 (Z) is added to the ascii value of the inputted letter and subtracted by 65
            decrypt = decrypt + newletter
        elif 97 <= ord(letter) <= 122: # Did the same for lowercase letters
            newletter = chr(122 - (ord(letter) - 97)) 
            decrypt = decrypt + newletter
        else:
            decrypt = decrypt + letter
    return decrypt

def decrypt_A1Z26(str): # 
    for letter in str:
        if letter.isalpha(): # if letter is in alphabet
            return str
    decrypt = "" # list for decrypt message
    space_remover = str.split(" ") # Split the space in between the numbers
    specialCharacters = ['.',',','?','"',"'","#","$","%","&","*","+","-","_","!"] # Made a spec. char list
    empty_list = []
    for element in space_remover:
        empty_list = element.split("-") # split the dash
        for numbers in empty_list: 
            expression = True
            for character in numbers:
                if character in specialCharacters: # If the character is a special character, it will do this
                    specialCharacter_finder = numbers.find(character) # Finds the character
                    decrypt += chr(65 + (int(numbers[0:specialCharacter_finder])-1))
                    decrypt += numbers[specialCharacter_finder]
                    expression = False
            if expression:
                numbers = int(numbers) 
                decrypt += chr(65+numbers-1)
        decrypt += ' '
    return decrypt
def main():
    text = input("Enter a text to decipher: ") # Print statements for version 4
    print("Let's try all the methods we have:")
    print(f"Ceaser cipher: {decrypt_ceaser(text, -3)}")
    print(f"Atbash cipher: {decrypt_atbash(text)}")
    print(f"Combined: 1) Ceaser; 2) Atbash Cipher: {decrypt_atbash(decrypt_ceaser(text, -3))}")
    print(f"Combined: 1) Atbash; 2) Ceaser Cipher: {decrypt_ceaser(decrypt_atbash(text), -3)}")
    print(f"A1Z26 cipher: {decrypt_A1Z26(text)}")
    print(f"Combined: 1) A1Z26; 2) Ceaser Cipher: {decrypt_ceaser(decrypt_A1Z26(text), -3)}")
    print(f"Combined: 1) A1Z26; 2) Atbash Cipher: {decrypt_atbash(decrypt_A1Z26(text))}")
    print(f"Combined: 1) A1Z26; 2) Atbash; 3) Ceaser Cipher: {decrypt_ceaser(decrypt_atbash(decrypt_A1Z26(text)), -3)}")
    print(f"Combined: 1) A1Z26; 2) Ceaser; 3) Atbash Cipher: {decrypt_atbash(decrypt_ceaser(decrypt_A1Z26(text), -3))}")
main()
