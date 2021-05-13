a, b, c = map(int, input().split())

n_5 = 0
n_7 = 0

if a == 5:
    n_5 +=1
elif a == 7:
    n_7 +=1

if b == 5:
    n_5 +=1
elif b == 7:
    n_7 +=1

if c == 5:
    n_5 +=1
elif c == 7:
    n_7 +=1

if n_5 == 2 and n_7 == 1:
    print("YES")
else:
    print("NO")