n,l = map(int,input().split())
S = []
for i in range(n):
    S.append(input())
print("".join(map(str,sorted(S))))