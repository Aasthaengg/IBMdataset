w = input()
s = list(set(w))

for i in range(len(s)):
    if w.count(s[i]) % 2 != 0:
        print('No')
        exit()
        
print('Yes')