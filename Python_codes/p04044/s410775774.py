n,l = map(int, input().split())
s = [str(input()) for i in range(n)]
s.sort()
w = ""
for h in s:
    w += h
print(w)