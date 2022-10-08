def decrypt_A1Z26(str):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    decrypt = []
    space_remover = str.split(" ")

    for numbers in str:
        current_word = ""
        current_numbers = numbers.split("-")
        for i in current_numbers:
            i = int(i)
            letter = alphabet_lower[i-1]
            current_word += letter
        decrypt.append(current_word)

    final = " ".join(decrypt)
    return final







print(decrypt_A1Z26("22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14"))