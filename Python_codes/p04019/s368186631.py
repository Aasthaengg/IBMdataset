S = input()
NEWS = {'N':0, 'E':0, 'W':0, 'S':0}
for char in S:
    NEWS[char] = 1
if NEWS['N']^NEWS['S'] | NEWS['E']^NEWS['W']:
    print("No")
else:
    print("Yes")