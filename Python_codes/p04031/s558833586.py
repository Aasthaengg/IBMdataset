N = int(input())
A = list(map(int,input().split()))
cost = []

for n in range(min(A),max(A)+1):
  cost.append(sum([(a-n)**2 for a in A]))

print(min(cost))