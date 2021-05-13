S=input()
t=set()
for i in range(len(S)):
    t.add(S[i])
if len(t)==4:
    print('Yes')
elif len(t)==3:
    print('No')
elif len(t)==2:
    if 'N' in t and 'S' in t:
        print('Yes')
    elif 'W' in t and 'E' in t:
        print('Yes')
    else:
        print('No')
else:
    print('No')