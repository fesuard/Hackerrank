# Implement a function that takes a string consisting of words separated by single spaces and 
# returns a string containing all those words but in reverse order and such that all cases of 
# letters in the original string are swapped, i.e. lowercase letters become uppercase and 
# uppercase letters become lowercase


def reverse_words_order_and_swap_cases(sentence):
    string_lst = sentence.split(' ')
    reverse_lst = string_lst[::-1]
    res_lst = []
    for word in reverse_lst:
        word_reverse = ''
        for letter in word:
            if letter.isupper():
                word_reverse += letter.lower()
            else:
                word_reverse += letter.upper()
        res_lst.append(word_reverse)
    return ' '.join(res_lst)
    
