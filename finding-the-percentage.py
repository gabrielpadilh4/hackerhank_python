# https://www.hackerrank.com/challenges/finding-the-percentage/problem

def average(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    result = round(average(student_marks[query_name]), 2)

    print("{:.2f}".format(result))
