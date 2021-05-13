s = input()

a = 'N' in s
b = 'S' in s
c = 'E' in s
d = 'W' in s

ans = 'Yes' if all([a == b, c == d]) else 'No'
print(ans)
