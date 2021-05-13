n,l = map(int,input().split())
s_list = []

for i in range(n):
    s = input()
    s_list.append(s)

s_list_sorted = sorted(s_list)

for s_i in s_list_sorted:
    print(s_i,end = "")