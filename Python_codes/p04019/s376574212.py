s= list(set(input()))
print('No' if s.count('N')!=s.count('S') or s.count("W") !=s.count('E') else 'Yes')