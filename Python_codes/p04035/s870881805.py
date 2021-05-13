N,L = map(int,input().split())
A = list(map(int,input().split()))

last = -1
for i,(a,b) in enumerate(zip(A,A[1:])):
    if a+b >= L:
        last = i+1
        break
else:
    print('Impossible')
    exit()

print('Possible')
ans = [n for n in range(1,last)] + [n for n in range(N-1,last,-1)]
ans.append(last)
print(*ans, sep='\n')