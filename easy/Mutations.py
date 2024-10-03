# https://www.hackerrank.com/challenges/python-mutations/problem
# Read a given string, change the character at a given index and then print the modified string.
# Complete the mutate_string function in the editor below.


#using string slicing:
def mutate_string(string, position, character):
    res = string[:position] + character + string[position + 1:]
    return res


#using list conversion:
def mutate_string1(string, position, character):
    res = list(string)
    res[position] = character
    return "".join(res)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
