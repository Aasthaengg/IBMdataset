S = input()
n,w,e,s = 'N' in S, 'W' in S, 'E' in S, 'S' in S
print('Yes' if n == s and e == w else 'No')