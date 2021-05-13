h,w,a,b =map(int,input().split())
mod = 10**9+7

#階乗を求める
fact_l = [1 for i in range(h+w+1)]
for i in range(1,len(fact_l)):
    fact_l[i] *= (fact_l[i-1]*i)%mod

#逆元
factinv_l = [1 for i in range(h+w+1)]
for i in range(1,len(fact_l)):
    factinv_l[i] = pow(fact_l[i],mod-2,mod)
    
#必ず通るポイントまでの組み合わせ
point1 = [1 for i in range(w-b)]
for i in  range(len(point1)):
    yoko = b+i 
    tate = h-a-1
    n = yoko+tate
    r = yoko
    point1[i] = fact_l[n]*factinv_l[r]*factinv_l[n-r]%mod

#point1からの経路
out = 0
for i in range(len(point1)):
    yoko = w-b-i-1
    tate = a-1
    n = yoko+tate
    r = yoko
    case = fact_l[n]*factinv_l[r]*factinv_l[n-r]%mod
    out += (point1[i]*case)%mod
print(out%mod)