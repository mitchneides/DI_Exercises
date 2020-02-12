#1
#
# import random
#
#
# def get_words_from_file():
#     word_list = []
#     with open('word_list.txt','r') as file:
#         text = file.read()
#     for word in str(text).split('\n'):
#         word_list.append(word)
#     return word_list
#
#
# def get_random_sentence(length):
#     all_word_list = get_words_from_file()
#     word_dict = {}
#     short_word_list = []
#     for round in range(length):
#         rand_index = random.randint(0,len(all_word_list))
#         word_dict[round] = all_word_list[rand_index]
#     for value in word_dict.values():
#         short_word_list.append(value.lower())
#     sentence = " ".join(short_word_list)
#     print(f"Your random sentence of {length} words: {sentence}.")
#     return sentence
#
#
# def main():
#     print("This program generates a random sentence at the length of your choosing.")
#     l = int(input("How many words would you like in the sentence? \nEnter a positive integer between 2 and 20: "))
#     if 2<=l<=20:
#         get_words_from_file()
#         get_random_sentence(l)
#     else:
#         raise KeyError("Invalid input. Goodbye.")
#
#
# if __name__ == '__main__':
#     main()


# 2

menu = {
    'starters': {
        'fries': 20,
        'house salad': 25,
        'wings': 30
    },
    'entres': {
        'burger': 55,
        'chicken': 50,
        'steak': 65
    },
    'deserts': {
        'brownie': 20,
        'cake': 25,
        'cookie': 15
    },
    'drinks': {
        'cola': 12,
        'beer': 15,
        'wine': 15
    }
}

import json

with open("menu.json","w") as file:
    json.dump(menu,file)