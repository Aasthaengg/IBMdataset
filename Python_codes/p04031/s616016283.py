n= int(input())
a= list(map(int,input().split()))
maxa,mina=max(a),min(a)
if maxa==mina:print(0)
else:
    gmin=9999999
    for c in range(mina,maxa+1):gmin=min(gmin,sum([(c-b)*(c-b) for b in a]))
    print(gmin)