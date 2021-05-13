N, L = [int(x) for x in input().split()]

seq = []

for i in range(N):
    seq.append(input())
    seq = sorted(seq)

ans = ''
for i in range(N):
    ans += seq[i]

print(ans)