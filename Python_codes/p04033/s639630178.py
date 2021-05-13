a,b = list(map(int,input().split()))

if a>0:
    out = "Positive"
elif a<=0 and 0<=b:
    out = "Zero"
else:
    C = b-a
    if C%2==1:
        out = "Positive"
    else:
        out = "Negative"
print(out)
