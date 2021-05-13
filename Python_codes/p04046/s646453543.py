def main():
    h,w,a,b=map(int,input().split(' '))
    mod = 10**9+7
    mx=max(h,w)
    fac=[1]*(h+w+1)
    for i in range(1,h+w+1):
        fac[i]=fac[i-1]*i%mod
    rev=[1]*(mx+1)
    rev[-1]=pow(fac[mx],mod-2,mod)
    for i in range(mx-1,-1,-1):
        rev[i]=rev[i+1]*(i+1)%mod
    const=rev[h-a-1]*rev[a-1]%mod
    ans = sum(fac[h - a + i - 1] * rev[i] * fac[a + w - 2 - i] * rev[w - i - 1] % mod for i in range(b, w))
    print(ans * const % mod)



if __name__ == '__main__':
    main()
