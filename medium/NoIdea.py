# https://www.hackerrank.com/challenges/no-idea/problem
# There is an array of integers. There are also disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
# For each integer i in the array, if i in A you add 1 to your happiness. If i in B, you add -1
# to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.


def get_happiness(arr, set_a, set_b):
    res = 0
    for elem in arr:
        if elem in set_a:
            res += 1
        elif elem in set_b:
            res -= 1
    print(res)
    

if __name__ == '__main__': 
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    get_happiness(arr, set_a, set_b)
    
