N = int(input())
A_list = []
for i in range(N):
    A = int(input())
    A_list.append(A)
# print(A_list)

ans = 0
tmp = 0
for i in range(len(A_list)):
    if A_list[i] != 0:
        if i == len(A_list)-1:
            tmp += A_list[i]
            ans += int(tmp/2)
        else:
            tmp += A_list[i]
    else:
        ans += int(tmp/2)
        tmp = 0

print(ans)