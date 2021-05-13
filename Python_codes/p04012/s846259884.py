N = input()
ans_num = 0
# 重複を消して抽出する
set_N = list(set(N))
for i in set_N:
    if N.count(i) % 2 == 1:
        ans_num = 1
        break
    else:
        continue
if ans_num == 0:
    print('Yes')
else :
    print('No')