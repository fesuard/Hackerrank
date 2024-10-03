# https://www.hackerrank.com/challenges/nested-list/problem
# Given the names and grades for each student in a class of N students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.Note: If there are multiple 
# students with the second lowest grade, order their names alphabetically and print each name on a 
# new line.


def student_grade(records):
    sorted_keys = sorted(records.keys())
    second_lowest = sorted_keys[1]
    names = records[second_lowest]
    names.sort()
    for name in names:
        print(name)

if __name__ == '__main__':
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in records:
            records[score] = [name]
        else:
            records[score].append(name)
    student_grade(records)
                               
