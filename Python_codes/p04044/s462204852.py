n, l = map(int, input().split())

s = [input() for _ in range(n)]
s.sort()

for string in s:
    print(string, end='')