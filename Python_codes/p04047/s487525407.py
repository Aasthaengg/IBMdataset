n = input()
L = [int(_) for _ in input().split()]
L.sort()

total = 0

for i in range(len(L)):
    if i % 2 == 0:
        total += L[i]
        
print(total)