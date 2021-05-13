n = int(input())
a = list(map(int,input().split()))
a.sort()
mean = sum(a)//n
ansl = 0
anss = 0
for i in range(n):
    ansl += (a[i]-mean)**2
    anss += (a[i]-mean-1)**2

print(min(ansl,anss))

