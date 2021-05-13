#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

n,l = map(int, input().split())

strs = []
for i in range(n):
    strs.append(input())

for i in range(1,l+1):
    strs.sort(key=lambda x:x[l-i])

for i in range(n):
    print(strs[i], end="")

