h,w,a,b=map(int,input().split())
n_func=[None for _ in [0]*200001]
n_func[0]=1
for i in range(1,200001):
    n_func[i]=(i*n_func[i-1])%(10**9+7)
def inv_n(n,mod=10**9+7):return pow(n,mod-2,mod)
def nCr(n,r,mod=10**9+7):return inv_n(n_func[n-r]*n_func[r]%mod,mod)*n_func[n]%mod

cnt=0
for i in range(h-a):
    cnt=(cnt+nCr(i+b-1,b-1)*nCr(h+w-b-i-2,w-b-1))%(10**9+7)
print(cnt)