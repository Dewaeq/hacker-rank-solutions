students = list()

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    
second_lowest = sorted(list(set(x[1] for x in students)))[1]
desired_students = [x[0] for x in students if x[1] == second_lowest]
print("\n".join(sorted(desired_students)))