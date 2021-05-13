A = list(map(int, input().split()))

A_sort = sorted(A)

if A_sort[0]==5 and A_sort[1]==5 and A_sort[2]==7:
    print("YES")
else:
    print("NO")
