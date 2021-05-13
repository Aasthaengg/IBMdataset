from collections import defaultdict
d=defaultdict(int)
s=input()
for i in s:
    d[i]+=1
for v in d.values():
    if v%2==1:
        print("No")
        exit()
print("Yes")