# https://www.hackerrank.com/challenges/python-lists/problem
# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i, print: Print the list, remove e: Delete the first 
# occurrence of integer e, append e: Insert integer e at the end of the list, sort: Sort the list
# pop: Pop the last element from the list, reverse: Reverse the list. Initialize your list and 
# read in the value of followed by lines of commands where each command will be of the types listed
# above. Iterate through each command in order and perform the corresponding operation on your list. 


if __name__ == '__main__':
    N = int(input())
    res_lst = []
    for _ in range(N):
        command, *line = input().split()
        values = tuple(map(int, line))
        if command == 'insert':
            res_lst.insert(values[0], values[1])
        if command == 'print':
            print(res_lst)
        if command == 'remove':
            res_lst.remove(values[0])
        if command == 'append':
            res_lst.append(values[0])
        if command == 'sort':
            res_lst.sort()
        if command == 'pop':
            res_lst.pop()
        if command == 'reverse':
            res_lst.reverse()
