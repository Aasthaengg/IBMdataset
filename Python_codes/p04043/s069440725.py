arr = list(map(int, input().split()))
arr.sort()
if (arr[0] == 5) and (arr[1] == 5) and (arr[2] == 7):
    print("YES")
else:
    print("NO")