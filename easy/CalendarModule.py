# https://www.hackerrank.com/challenges/calendar-module/problem
# You are given a date. Your task is to find what the day is on that date.
# Input Format
# A single line of input containing the space separated month, day and year, 
# respectively, in MM DD YY format. Output the correct day in capital letters.
import calendar

if __name__ == '__main__':
    weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    date = list(map(int, input().split()))
    day = calendar.weekday(date[2], date[0], date[1])
    print(weekdays[day])
