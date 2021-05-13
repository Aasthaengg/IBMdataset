N,L = map(int,input().split())
str_list=[]
final_str = ""
for i in range(N):
    str_list.append(input())
new_list = sorted(str_list)
for n in range(N):
    final_str += new_list[n]
print(final_str)