s = input()
p = ['N', 'S', 'E', 'W']
cnt = []
for i in p:
    cnt.append(s.count(i))
if cnt[0] != 0 and cnt[1] != 0 or cnt[0] == 0 and cnt[1] == 0:
    if cnt[2] != 0 and cnt[3] != 0 or cnt[2] == 0 and cnt[3] == 0:
        print("Yes")
    else:
        print("No")
elif cnt[2] != 0 and cnt[3] != 0 or cnt[2] == 0 and cnt[3] == 0:
    if cnt[0] != 0 and cnt[1] != 0 or cnt[0] == 0 and cnt[1] == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")