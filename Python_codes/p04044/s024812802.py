N, L = [int(x) for x in input().split()]
S_list = []
for i in range(N):
    S_list.append(input())
    
S = ''.join(sorted(S_list))
print(S)