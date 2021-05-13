N=int(input())
Ln=list(map(int,input().split()))
print(sum(sorted(Ln)[::2]))
