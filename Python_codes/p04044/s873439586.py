N, L = map(int,input().split())
str_list = [input() for i in range(N)]

str_list.sort()
ans = "".join(str_list)
print(ans)