#sys.setrecursionlimit(10**7)
#inf = 10**9
sum=0
N=int(input())
A=int(input())
sum+=A//2
a=A%2
for _ in range(1,N):
    A=int(input())
    if a==1 and A>0:
        sum+=a
        A-=a
        a=0
    sum+=A//2
    a=A%2
print(sum)




