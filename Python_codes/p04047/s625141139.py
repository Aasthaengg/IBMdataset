a = int(input())
s = input().split()
d = []
m = 0
for i in s:
    d.append(int(i))
while d != []:
    d.remove(max(d))
    m += max(d)
    d.remove(max(d))
print(m)
