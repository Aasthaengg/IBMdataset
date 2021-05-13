N = int(input())
a = list(map(int,input().split()))
ans = []

avg = 0
if (max(a)+min(a))%2 == 0:
    avg = (max(a)+min(a))/2
else:
    avg = (max(a)+min(a))/2+1

for i in range(-100,101,1):
    sum = 0
    for j in a:
        sum += (j-i)**2
    ans.append(sum)
    
print(min(ans))