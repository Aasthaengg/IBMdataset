N = 3

a, b, c = [int(N) for N in input().split() ]

d = 17

mylist = [5, 7]

if ( a in mylist and b in mylist and c in mylist and a + b + c == 17 ):
    print("YES")
else:
    print("NO")
