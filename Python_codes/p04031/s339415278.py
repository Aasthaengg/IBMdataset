N = int(input())
a = list(map(int,(input().split())))
nim = float("inf")
for i in range(-100,101):
    s = 0
    for j in a:
        s += (i-j)**2
    nim = min(nim,s)
print(nim)