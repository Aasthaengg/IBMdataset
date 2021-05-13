w = input()

if len(w) % 2 != 0:
    print('No')
    exit()

cnt = [0]*30
for i in range(len(w)):
    a = ord(w[i]) - ord('a')
    cnt[a] += 1

for i in range(len(cnt)):
    if cnt[i] % 2 != 0:
        print('No')
        exit()

print('Yes')