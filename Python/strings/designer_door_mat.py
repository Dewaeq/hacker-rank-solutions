height, width = map(int, input().split())

word = 'WELCOME'
pattern = [('.|.' * (2 * i + 1)).center(width, '-') for i in range(height // 2)]

for i in pattern:
    print(i)
print(word.center(width, '-'))


for i in reversed(pattern):
    print(i)
