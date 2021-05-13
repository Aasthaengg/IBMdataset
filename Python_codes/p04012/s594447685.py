s=input()
n=0
while True:
    i=s[0]
    if s.count(i) % 2 == 0:
        s=s.replace(i,'')
        if s == '':
            break
        continue
    n+=1
    break
print('YNeos'[n::2])
