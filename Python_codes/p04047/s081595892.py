n = int(input())
L = list(map(int, input().split()))
L.sort()
array_L = []
for m in [i * 2 for i in range(n)]:
    array_L.append(L[m])
print(sum(array_L))
    
