A, B, C = [int(x) for x in input().split()]
req_fives = 2
req_seven = 1
for x in (A, B, C):
    if x == 5:
        req_fives -= 1
    elif x == 7:
        req_seven -= 1
if req_fives == 0 & req_seven == 0:
    print("YES")
else:
    print("NO")