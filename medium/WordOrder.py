# https://www.hackerrank.com/challenges/word-order/problem
# You are given n words. Some words may repeat. For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word. See the sample


def word_order(n):
    words = {}
    res = ''
    for _ in range(n):
        word = input()
        words[word] = words.get(word, 0) + 1
    print(len(words.keys()))
    for number in words.values():
        res += str(number) + ' '
    print(res)


if __name__ == '__main__':
    n = int(input())
    word_order(n)
