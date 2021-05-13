n,l = [int(x) for x in input().split()]
ss = [ input() for x in range(n)]
#print(ss)
ss.sort()
#print(ss)
print(''.join(ss))