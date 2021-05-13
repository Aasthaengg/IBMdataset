n = int(input())
hold = 0
res = 0
for i in range(n):
    a = int(input())
    if i==0:
        res += a//2
        hold = a%2
    else:
        if a < hold:
            res += a
            hold = 0
        else:
            res += hold
            a -= hold
            res += a//2
            hold = a%2
print(res)