n, m = map(int, input().split())
li = []
for i in range(n):
    s = input()
    li.append(s)
li.sort()
for i in li:
    print(i, end="")
