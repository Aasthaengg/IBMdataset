s= list(input())
s=set(s)
if len(s)%2==1:
    print('No')
else:
    if len(s) == 2:
        if "W" in s and "E" in s or "S" in s and "N" in s:
            print("Yes")
        else:
            print('No')
    else:
        print('Yes')
