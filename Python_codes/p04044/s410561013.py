n,l=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
l.sort()
for a in l:
    print(a,end="")