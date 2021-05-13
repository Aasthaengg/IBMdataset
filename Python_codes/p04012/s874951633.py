# coding: utf-8
w = list(input())

w_ = list(set(w))
flg = True
for a in w_:
    if w.count(a)%2 != 0:
        flg = False

if flg:
    print("Yes")
else:
    print('No')