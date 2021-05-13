s=input()
for i in s:
    if s.count(i)%2!=0:
        print('No')
        exit()
print('Yes')
