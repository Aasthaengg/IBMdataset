s=input()
ss=set(s)
a=["N","W","S","E"]
flg=False
if all(a[i] in s for i in range(4)):
    flg=True
if a[0] in s and a[1] not in s and a[2] in s and a[3] not in s:
    flg=True
if a[0] not in s and a[1] in s and a[2] not in s and a[3] in s:
    flg=True
if flg:
    print("Yes")
else:
    print("No")