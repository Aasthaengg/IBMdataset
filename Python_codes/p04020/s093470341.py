from collections import Counter
n = int(input())
count=0
res = 0
for _ in range(n):
  a = int(input())
  if res < a:
    tmp = (a-res)%2
    count += res+(a-tmp-res)//2
    res = tmp
  else:
    count += a
    res = 0
    
print(count)