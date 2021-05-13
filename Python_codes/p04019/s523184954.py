# coding: utf-8
# Your code here!
#a, b = map(int,input().split())
S = input()
F = [False] * 4
n = len(S)
flg = False
V = ["E", "W", "N", "S"]
for i in range(n):
    s = S[i]
    F[V.index(s)] = True

if not (F[0]^F[1]):
    if not (F[2]^F[3]):
        flg = True
a = True
b=  False
c=False
if flg:
    print("Yes")
else:
    print("No")

#print(a^b, b^c)
