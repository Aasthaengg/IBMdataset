n = int(input())

al = [int(input()) for _ in range(n)]

if n == 1:
    print(al[0] // 2 * 2 // 2)
    exit()
ans = 0
for i in range(n-1):
    rest = ((al[i] + al[i+1]) // 2) * 2
    ans += rest
    for j in range(2):
        if al[i+j] >= rest:
            al[i+j] -= rest
            break
        else:
            rest -= al[i+j]
            al[i+j] = 0


print(ans//2)