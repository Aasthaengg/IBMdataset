a=input()
s=[0]*26
for i in range(len(a)):
    s[ord(a[i])-ord("a")]+=1
for i in range(26):
    if s[i]%2!=0:
        print("No")
        break
else:
    print("Yes")