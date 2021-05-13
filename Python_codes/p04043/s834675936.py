num = list(map(int, input().split()))

ans = sorted(num)
if(ans[0]==5 and ans[1]==5 and ans[2] == 7):
    print("YES")
else:
    print("NO")