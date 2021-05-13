s = input()
list_s = list(set(s))
ans = ''
if len(set(s)) == 4:
    ans = 'Yes'
elif len(list_s) == 2 and list_s.count('E') == list_s.count('W'):
    ans = 'Yes'
elif len(list_s) == 2 and list_s.count('N') == list_s.count('S'):
    ans = 'Yes'
else:
    ans = 'No'
print(ans)