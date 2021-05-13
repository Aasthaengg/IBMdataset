w=input()
x=set(w)
for i in x:
    if w.count(i)%2!=0:
        print('No')
        break
else:
    print('Yes')