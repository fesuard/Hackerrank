# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# You are the manager of a supermarket. You have a list of N items together with their prices that consumers bought on a 
# particular day. Your task is to print each item_name and net_price in order of its first occurrence.
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.
# The first line contains the number of N items. The next N lines contains the item's name and price, separated by a space.
from collections import OrderedDict


if __name__ == '__main__':
    n = int(input())
    dic = OrderedDict()
    for _ in range(n):
        item_name, space, net_price = input().rpartition(' ')
        if item_name in dic:
            dic[item_name] += int(net_price)
        else:
            dic[item_name] = int(net_price)
    for key, value in dic.items():
        print(key + ' ' + str(value))
