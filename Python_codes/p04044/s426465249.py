N,L= map(int,input().split())
list=[]
for I in range(N):
    S=str(input())
    list.append(S)
list.sort()
c="".join(list)
print(c)