from collections import deque
S=input()
ans=[]
ans=deque(ans)
for letter in S:
    if letter=='0':
        ans.append('0')
    elif letter=='1':
        ans.append('1')
    else:
        if len(ans)!=0:
            ans.pop()

print(''.join(ans))