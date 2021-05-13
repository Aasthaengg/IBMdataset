N = int(input())
r = 0
b = 0
for _ in range(N):
    a = int(input())
    a += b
#    print(a-b,b,a//2)
    r += a//2
    if a == 1 and b == 1:
        b = 0
    elif a%2:
        b = 1
    else:
        b = 0
print(r)
