# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a
# list of students. Print the average of the marks array for the student name provided, showing 2
# places after the decimal. 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_grade = sum(student_marks[query_name])/len(student_marks[query_name])
    formatted_avg = f"{avg_grade:.2f}"
    print(formatted_avg)
