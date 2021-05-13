import sys
input = sys.stdin.buffer.readline
import copy

def main():
    H,W,A,B = map(int,input().split())
    MOD = 10**9+7
    fac = [0 for _ in range(H+W+1)]
    fac[0],fac[1] = 1,1
    inv = copy.deepcopy(fac)
    invfac = copy.deepcopy(fac)
    
    for i in range(2,H+W+1):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = MOD-(MOD//i)*inv[MOD%i]%MOD
        invfac[i] = (invfac[i-1]*inv[i])%MOD
        
    def coef(x,y):
        num = (((fac[x+y]*invfac[x])%MOD)*invfac[y]%MOD)
        return num

    ans = 0
    for i in range(H-A):
        able = coef(i,B-1)*coef(H-i-1,W-B-1)
        ans += able
        ans %= MOD
        
    print(ans)  

if __name__ == "__main__":
    main()
