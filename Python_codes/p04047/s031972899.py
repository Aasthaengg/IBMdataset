num = int(input())
num *= 2
Skewers = list(map(int, input().split()))
 
Skewers.sort()
val = 0
for i in range(0, num-1, 2):
  val += min(Skewers[i], Skewers[i + 1])
  
  
print(val)