# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Given sets of integers, M and, N print their symmetric difference in ascending order. The term symmetric
# difference indicates those values that exist in either M or N but do not exist in both. Output the symmetric
# difference integers in ascending order, one per line.


def symmetric_difference(a, b):
    res = []
    res.extend(list(a - b))
    res.extend(list(b - a))
    res.sort()
    for elem in res:
        print(elem)


if __name__ == '__main__':
    n1 = int(input())
    set1 = set(map(int, input().split()))

    n2 = int(input())
    set2 = set(map(int, input().split()))

    symmetric_difference(set1, set2)
    
