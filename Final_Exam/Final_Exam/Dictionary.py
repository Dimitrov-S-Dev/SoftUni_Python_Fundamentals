def get_test(words_lst, dic):
    for word in words_lst:
        if word in dic.keys():
            print(f"{word}:")
            for element in dic[word]:
                print(f"-{element}")



def get_hand_over(dic):
    result = []
    for word in dic.keys():
        result.append(word)
    print(" ".join(result))



def get_dictionary(number):
    dictionary_dict = {}
    test_words = []
    for num in range(number):
        if num == 0:

            info = input().split(" | ")
            for element in info:
                if ":" in element:
                    word, definitions = element.split(": ")
                    if word not in dictionary_dict.keys():
                        dictionary_dict[word] = []
                    dictionary_dict[word].append(definitions)
        elif num == 1:
            words = input().split(" | ")
            for word in words:
                test_words.append(word)

        elif num == 2:
            command = input()
            if command == "Test":
                get_test(test_words, dictionary_dict)
            else:
                get_hand_over(dictionary_dict)


get_dictionary(3)
