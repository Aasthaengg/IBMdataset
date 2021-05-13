N = int(input())

s = list(map(int,input().split()))

s.sort()

sum = 0

for i in range(N):
  sum = sum + s[2*i]

print(sum)