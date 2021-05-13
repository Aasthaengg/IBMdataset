nl = list(map(lambda x: int(x), input().split(" ")))
n = nl[0]
l = nl[1]

strs = [input() for i in range(n)]

strs.sort()

print(''.join(strs))
