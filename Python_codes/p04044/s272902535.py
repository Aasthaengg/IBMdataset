n,l = map(int,input().split())
string_list=[input() for i in range(n)]

string_list.sort()
for X in string_list:
  print(X, end="")