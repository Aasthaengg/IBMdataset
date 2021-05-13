L = list(map(int,input().split()))
cnt = 0

for i in range(3):
         cnt += L[i]
         
if cnt == 17:
         print("YES")

else:
         print("NO")