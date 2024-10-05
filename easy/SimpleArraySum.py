# https://www.hackerrank.com/challenges/simple-array-sum/problem
# Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
# simpleArraySum has the following parameter(s):


def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
