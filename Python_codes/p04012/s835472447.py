str1 = input()
wo = list(str1)
li = [0 for i in range(26)]
for i in range(len(wo)):
    li[ord(wo[i])-97] += 1
flag = True
for i in range(26):
    if li[i] % 2 != 0:
     flag = False
if flag:
    print('Yes')
else:
    print('No')