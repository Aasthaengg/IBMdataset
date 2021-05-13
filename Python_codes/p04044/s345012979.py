n,l = map(int,input().split())
s = list(input() for i in range(n))
s.sort()
print(''.join(s))