N = int(input())
L = list(map(int,input().split()))
L.sort(reverse=True)
#print(L)

cnt = 0
for l in L[1::2]:
    #print(l)
    cnt += l

print(cnt)