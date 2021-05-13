N, L = map(int, input().split())
str_list = []
for i in range(N):
  str_list.append(input())

print("".join(sorted(str_list)))