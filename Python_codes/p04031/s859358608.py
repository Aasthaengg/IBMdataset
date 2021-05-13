N = int(input())
A = list(map(int,input().split()))
m = round(sum(A)/N)
print(sum((a-m)**2 for a in A))