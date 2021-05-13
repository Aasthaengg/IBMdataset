n,l=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(input())
lst.sort()
print("".join(lst))