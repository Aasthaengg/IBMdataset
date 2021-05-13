a,b=map(int,input().split())
l=[]
for i in range(a):
    a=input()
    l.append(a)
print("".join(map(str,sorted(l))))