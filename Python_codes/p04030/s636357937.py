s=input()
t=''
for c in s:
    if c!='B':
        t+=c
    elif t!='':
        t=t[:-1]
print(t)