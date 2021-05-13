w = list(input())
al = list("abcdefghijklmnopqrstuvwxyz")
for i in al:
    if w.count(i)%2==1:
        print("No")
        break
else:
    print("Yes")