
#     Ask a user for a word.
#     Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
#         Make sure the letters are the keys.
#         Make sure the letters are strings.
#         Make sure the indexes are stored in a list, and those lists are values.

# Examples

#     “dodo” ➞ { “d”: [0, 2], “o”: [1, 3] }
#     “froggy” ➞ { “f”: [0], “r”: [1], “o”: [2], “g”: [3, 4], “y”: [5] }
#     “grapes” ➞ { “g”: [0], “r”: [1], “a”: [2], “p”: [3], “e”: [4], “s”: [5] }
user_word=input("enter a word: ")
dict_letter_indexes={}
for index in range(len(user_word)):
    letter=user_word[index]
    if letter in dict_letter_indexes:
        dict_letter_indexes[letter].append(index)
    else:
        dict_letter_indexes[letter]=[index]
print(dict_letter_indexes)



