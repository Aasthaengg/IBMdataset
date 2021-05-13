a,b = [int(i) for i in input().split()]
pala = []
for i in range(a) : pala.append(input())
pala.sort()
print("".join(map(str,pala)));
