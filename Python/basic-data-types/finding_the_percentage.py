students = list()
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    students.append([name, scores])
query_name = input()

student_scores = list([x[1] for x in students if x[0] == query_name])[0]
average = sum(student_scores)/len(student_scores)
print("{:.2f}".format(average))