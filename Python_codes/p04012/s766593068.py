import collections
S=list(input())
c = collections.Counter(S)
L=c.values()
for i in L:
  if i%2==1:
    print("No")
    exit()
print("Yes")