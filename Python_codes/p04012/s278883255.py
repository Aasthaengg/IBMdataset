w = input()
w_dict = {}
for char in w:
    if char in w_dict:
        w_dict[char] += 1
    else:
        w_dict[char] = 1

if all(elem%2 == 0 for elem in w_dict.values()):
    print('Yes')
else:
    print('No')