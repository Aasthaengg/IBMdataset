n, y = map(int, input().split())
A = list(map(str, [input() for i in range(n)]))
list.sort(A, reverse=False)
print(''.join(A))