n, l = map(int, input().split())
list = []
for i in range(n) :
    s = input()
    list.append(s)
list.sort()
print("".join(list))
