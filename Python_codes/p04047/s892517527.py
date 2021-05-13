from sys import stdin
point = 0
n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
li.sort()
for i in range(n):
    point += min(li[2*i],li[2*i+1])
print(point)