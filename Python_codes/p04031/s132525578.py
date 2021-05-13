N = int(input())
A = list(map(int,input().split()))
print(min(sum((a-n)**2 for a in A) for n in range(min(A),1+max(A))))