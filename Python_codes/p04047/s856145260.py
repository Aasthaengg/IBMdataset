n = int(input())
n *= 2
skewers = list(map(int, input().split()))

skewers.sort()
eats = 0
for i in range(0, n-1, 2):
  eats += min(skewers[i], skewers[i + 1])
  
  
print(eats)