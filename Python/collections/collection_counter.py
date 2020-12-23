from collections import Counter

x = int(input())                            # Number of shoes
sizes = Counter(map(int, input().split()))  # Shoe sizes
n = int(input())                            # Number of customers

earnings = 0

for _ in range(n):
    size, price = map(int, input().split())
    if size in sizes.keys() and sizes[size] > 0:
        earnings += price
        sizes[size] -= 1
        
print(earnings)