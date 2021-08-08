# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = True

    if(year % 400 == 0):
        return leap
    elif(year % 100 == 0):
        return not leap
    elif(year % 4 == 0):
        return leap
    else:
        return not leap


year = int(input())
print(is_leap(year))
