# https://www.hackerrank.com/challenges/collections-counter/problem
# Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.
# Input Format
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.


if __name__ == '__main__':
    no_of_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    no_of_customers = int(input())
    dic = {}
    for _ in range(no_of_customers):
        shoe_size, price = map(int, input().split())
        if shoe_size in shoe_sizes:
            dic[shoe_size] = dic.get(shoe_size, 0) + price
            shoe_sizes.remove(shoe_size)
    print(sum(dic.values()))
