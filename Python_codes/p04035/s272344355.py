N, L = map(int, input().split())
a = list(map(int, input().split()))
end = 0
for i in range(N - 1):
    if a[i] + a[i + 1] >= L:
        end = i + 1
        break
else:
    print('Impossible')
    exit()

ans = list(range(1, end)) + list(range(end, N))[::-1]
print('Possible')
print(*ans, sep='\n')