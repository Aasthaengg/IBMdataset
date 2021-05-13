w = list(input())
alphabet = list(chr(ord("a") + i) for i in range(26))
enumerate = [0]*26

for x in w:
    for i in range(26):
        if x == alphabet[i]:
            enumerate[i] += 1

ans = 0
for i in range(26):
    if enumerate[i]%2 != 0 and enumerate[i] > 0 :
        ans = 1

if ans == 1:
    print("No")
else:
    print("Yes")
