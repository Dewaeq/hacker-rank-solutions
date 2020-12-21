n = int(input())
grades = [int(input()) for x in range(n)]

for grade in grades:
    d = 5-(grade%5)
    if d < 3 and grade + d >= 40:
        grade += d
    print(grade)
