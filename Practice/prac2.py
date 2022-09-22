'''
vowels = ['a', 'e', 'i', 'o', 'u']
word_list = ['apples', 'crayons', 'scissors', 'markers', 'erasers', 'pencils', 'elephant']
# for word in word_list:
for index in range (0, len(word_list)):
    word = word_list[index]
    if word[0] in vowels:
        r_word = word_list.pop(index)
        word_list.insert(0, r_word)
print(word_list)
'''
vowels = ['a', 'e', 'i', 'o', 'u']
word_list = ['apples', 'crayons', 'scissors', 'markers', 'erasers', 'pencils', 'elephant']

for word in word_list:
    if word[0] in vowels:
        word_list.remove(word)
        word_list.insert(0, word)
print(word_list)



