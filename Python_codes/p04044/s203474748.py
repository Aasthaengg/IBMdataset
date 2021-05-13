a,b = list(map(int,input().split(" ")))

l = [input() for i in range(a)]

l.sort()
print("".join(l))