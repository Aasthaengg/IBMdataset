w = list(input())

w_set = set(w)
flag = 0

for l in w_set:
    if w.count(l)%2 != 0:
        print('No')
        flag = 1
        break

if flag==0:
    print('Yes')