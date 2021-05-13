a = int(input())
b = list(map(int,input().split()))
b = sorted(b)
c = 0
for i in range(0,2*a,2):
    c += b[i]
print(c)