H,W,A,B=map(int,input().split())

mod=10**9+7

n=H+W
INV=[None]*(n+1)#1/aのリストを予め作っておく.
for i in range(1,n+1):
    INV[i]=pow(i,mod-2,mod)

k=H+W-2
n=H-1
Combi1=[None]*(k+1)#Combi[i]=iCnを表す.kは必要な分だけ.
Combi1[n]=1
for i in range(n+1,k+1):
    Combi1[i]=Combi1[i-1]*i*INV[i-n] %mod

k=H+B-2
n=B-1
Combi2=[None]*(k+1)#Combi[i]=iCnを表す.kは必要な分だけ.
Combi2[n]=1
for i in range(n+1,k+1):
    Combi2[i]=Combi2[i-1]*i*INV[i-n] %mod

k=W-B-1+A
n=W-B-1
Combi3=[None]*(k+1)#Combi[i]=iCnを表す.kは必要な分だけ.
Combi3[n]=1
for i in range(n+1,k+1):
    Combi3[i]=Combi3[i-1]*i*INV[i-n] %mod




ANS=Combi1[H+W-2]
for x in range(H-A,H):
    ANS=(ANS-Combi2[x+B-1]*Combi3[(H-x-1)+W-B-1])%mod


print(ANS)