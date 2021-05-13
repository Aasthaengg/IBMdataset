N=input().split()
L_i = list(map(int, input().split()))

L_i.sort(reverse=False)

print(sum(L_i[0::2]))