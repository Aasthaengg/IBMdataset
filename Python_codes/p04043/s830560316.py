def haiku(A,B,C):

    list = [A,B,C]

    if(list.count(5) == 2 and list.count(7) ==1):
        print("YES")
    else:
        print("NO")

A,B,C = (int(x) for x in input().split())
haiku(A,B,C)