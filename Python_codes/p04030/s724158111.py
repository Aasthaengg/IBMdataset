n=''
for i in input():
    n=n[:-1] if i == 'B' else n+i
print(n)
