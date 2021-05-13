L=input().split()
A,B,C=int(L[0]),int(L[1]),int(L[2])
X=[5,7]
ans = []
for i in range(len(X)):
    ans.append([A,B,C].count(X[i]))
if ans == [2,1]:
  print("YES")
else:
  print("NO")