a,b = map(int,input().split())
x = []
for i in range(a):
    x.append(input())

print("".join(sorted(x)))