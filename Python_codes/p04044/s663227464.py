N,L=map(int,input().split())
S=[]
for i in range(N):
    S.append(input())
    
S.sort()
A=''
for i in S:
    A+=i
print(A)