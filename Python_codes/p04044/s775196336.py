n,l = map(int,input().split())
line = []
for i in range(n):
    line.append(input())
line.sort()
for i in range(n):
    print(line[i],end="")
print("")