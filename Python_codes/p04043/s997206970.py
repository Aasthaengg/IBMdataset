A=list(map(int,input().split()))

A.sort()
flag=0

if A[0]==5:
    if A[1]==5:
        if A[2]==7:
            print("YES")
            flag+=1

if flag==0:
    print("NO")
