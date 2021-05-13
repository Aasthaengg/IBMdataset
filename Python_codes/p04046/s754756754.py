H,W,A,B=map(int,input().split())
INF=10**9+7
x=[0]*(H+W-1)
x[0]=1
for i in range(1,H+W-1):
    x[i]=(i*x[i-1])%INF
y=[0]*(H+W-1)
y[-1]=pow(x[-1],10**9+5,INF)
for i in range(H+W-2,0,-1):
    y[i-1]=(y[i]*i)%INF
ans=0
for i in range(B,W):
    j=H-A-1
    ans+=(x[i+j]*y[i]*y[j])*(x[W-1-i+H-2-j]*y[H-2-j]*y[W-1-i])
    ans%=INF
print(ans)
