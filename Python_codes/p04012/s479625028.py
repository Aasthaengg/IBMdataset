#!/usr/bin/env python3

alpha = {
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
}

S = input()

flg = True
for a in alpha:
    if S.count(a) % 2 != 0:
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")
