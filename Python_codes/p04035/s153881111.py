#%%
n, l = map(int, input().split())
a = list(map(int, input().split()))

flag = False
for i in range(n-1):
    if a[i] + a[i+1] >= l:
        flag = True
        pos = i
if flag:
    print('Possible')
    for i in range(n-1):
        if i < pos:
            print(i+1)
        elif i == pos :
            break
    for i in range(n-2, -1, -1):
        if i > pos :
            print(i+1)
        elif i == pos :
            break
    print(pos+1)
else:
    print('Impossible')


#%%
