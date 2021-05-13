n = int(input()) * 2
l = input().split()
s = []
for i in range(n):
  s.append(int(l[i]))
s.sort(reverse=True)
sum  = 0
for qq in range(1,n,2):
  sum = sum + s[qq]
  
print(sum)