n=int(input())
a=[int(x) for x in input().split()]
a.sort()
ss=0
for i in range(0,len(a),2):
    ss+=min(a[i:i+2])
print(ss)