s=input()
stk=[]
for c in s:
    if c in '01':
        stk.append(c)
    elif stk:
        stk.pop()
 
print(''.join(stk))