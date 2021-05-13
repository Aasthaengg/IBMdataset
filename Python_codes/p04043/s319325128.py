a,b,c = map(int,input().split())#標準入力を行う
if (a == 5 or a== 7):
    if(b == 5 or b == 7):
        if(c == 5 or c == 7):
            if(a + b + c == 17):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
