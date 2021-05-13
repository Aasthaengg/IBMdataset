A, B, C = map(int, input().split())

a = str(A)
b = str(B)
c = str(C)

d = a+b+c

if d.count("5") == 2 and d.count("7") == 1:
    print("YES")
else:
    print("NO")