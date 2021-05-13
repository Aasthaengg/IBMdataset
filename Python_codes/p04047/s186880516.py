n = int(input())
l = sorted(map(int, input().split()))
x = 0
for i in range(0,len(l),2):
  x += min(l[i],l[i+1])
print(x)