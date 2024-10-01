# https://www.hackerrank.com/challenges/exceptions/problem
# You are given two values a and b. Perform integer division and print a/b.
# Print the value of a/b. In the case of ZeroDivisionError or ValueError, 
# print the error code.


def int_division(a,b):
    print(int(a//b))


if __name__ == "__main__":
    for _ in range(int(input())):
        
        try:
            a, b = map(int, input().split())
            int_division(a, b)
            
        except Exception as e:
            print("Error Code:", e)
            
    
