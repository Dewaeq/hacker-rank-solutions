import re

for _ in range(int(input())):
    # [7-9] checks the first digit, \d{9} means we need another 9 digits (10 in total)
    # '$' marks the end of a string or line
    pattern = r'[7-9]\d{9}$'
    if re.match(pattern, input()):
        print("YES")
    else:
        print("NO")
