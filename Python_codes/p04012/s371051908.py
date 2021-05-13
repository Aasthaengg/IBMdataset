s=input()
print('Yes'if all(s.count(i)%2==0for i in set(s))else'No')