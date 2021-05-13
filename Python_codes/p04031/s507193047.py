num = int(input())
l = list(map(int,input().split()))
min = 1000000
for n in range(-100,101):
  sum = 0
  for i in l:
    if n !=i:
      sum += (i-n)*(i-n)
  
  if min > sum:
    min = sum

print(min)