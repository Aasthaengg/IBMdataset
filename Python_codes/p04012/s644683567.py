w = input()
for i in range(len(w)):
    if w.count(w[i])%2==0:
        continue
    else:
        print('No')
        exit()
print('Yes')