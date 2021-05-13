S = str(input())
Flag = False

for i in S:
    if not S.count(i) % 2 == 0:
        Flag = True

if Flag:
    print('No')

else:
    print('Yes')
