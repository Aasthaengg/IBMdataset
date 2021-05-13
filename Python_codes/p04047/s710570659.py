a = int(input())
b = list(map(int,input().split()))
b.sort()
j = 0
num = 0
for i in range(a):
  c = b[j:j+2]
  num += min(c)
  j += 2
print(num)