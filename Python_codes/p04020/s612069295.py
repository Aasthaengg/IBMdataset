n = int(input())
a_list = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-1):
    cnt += a_list[i] // 2
    a_list[i] = a_list[i] % 2

    if a_list[i] == 1 and a_list[i+1] >= 1:
        cnt += 1
        a_list[i] = 0
        a_list[i+1] -= 1

# 最後に末尾のやつを処理する
cnt += a_list[n-1] // 2

print(cnt)