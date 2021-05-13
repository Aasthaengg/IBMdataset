#A[i]の部分列P[i]に0が含まれない場合、P[i]にあるカードを最大限利用し、sum(P[i])//2組構成でき、あまりは一切持ち越されない。
#これより、先頭から0が現れるまで要素を加算していき、0が出たら2で割って切り捨て
#この解はコーナーケースなくできる

#sum(P[i])//2組は何らかの順序でgreedyに取れば必ず構成でき、そうすることでP[i]のどこか1つがsum(P[i])%2となる以外は全て0となる
#... 0 [ P[i] ] 0 [ P[i+1] ]...と構成するため、
#... 0 [(1/0) 0 0 ... (0/1)] 0 [p[i+1][0] p[i+1][1] ...]があまりを活用できそうな最良配置だが、
#P[i]のあまりがあったときのあまり1はどのように扱ってもP[i-1],P[i+1]に活用できることはないとわかる


N=int(input())
A=[int(input()) for _ in range(N)]
cnt=0
buf=0
#print(A)
"""
if N==1:
    print(A[0]//2)
else:
    for i in range(N-1):
        su=A[i]+A[i+1]
        cnt=cnt+su//2
        buf=(su//2)*2
        if buf>A[i]:
            A[i+1]=A[i+1]-(buf-A[i])
            A[i]=0
        else:
            A[i]=A[i]-buf
    #print(A,cnt)
    print(cnt)
"""
su=0
for i in range(N):
    if A[i]!=0:
        su=su+A[i]
    else:
        cnt=cnt+su//2
        su=0
cnt=cnt+su//2
print(cnt)
