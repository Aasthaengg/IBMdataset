s = input()
for i in range(len(s)):
    s=s.replace('0B', '')
    s=s.replace('1B', '')
s=s.replace('B', '')
print(s)