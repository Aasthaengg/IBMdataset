a = input().strip()
lst=[]
for i in a:
    if i != " ":
        lst.append(i)
lst.sort()
if lst == ['5','5','7']:
    print("YES")
else:
    print("NO")