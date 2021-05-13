N,L = map(int, input().split())
string_list = [input() for i in range(N)]
string_list.sort()
print(''.join(string_list))