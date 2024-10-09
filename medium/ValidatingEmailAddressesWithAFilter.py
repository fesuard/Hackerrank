# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# You are given an integer N followed by N email addresses. Your task is to print a list 
# containing only valid email addresses in lexicographical order.
import re


def fun(s):
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    return re.match(pattern, s) is not None

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
