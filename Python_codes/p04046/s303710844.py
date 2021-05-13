import operator as op
from functools import reduce

MODULUS = 10**9 + 7

if __name__ == '__main__':
    [h, w, a, b] = map(int, input().split())

    # Taken from https://atcoder.jp/contests/abc042/submissions/3178794 for learning purposes.
    factorial = [0] * (h+w)
    factorial[0] = 1
    factorial[1] = 1
    inverse = [0] * (h+w)
    inverse[0] = 1
    inverse[1] = 1
    for i in range(2, h+w):
        factorial[i] = factorial[i-1] * i % MODULUS
        # フェルマーの小定理から(x! ** mod-2 % mod == x! ** -1 % mod)
        # powに第三引数入れると冪乗のmod付計算を高速にやってくれる
        inverse[i] = pow(factorial[i], MODULUS-2, MODULUS)
        
    # 組み合わせの数だけ返してくれる関数(自作)
    def ncr(n, r):
        # 10C7 = 10C3
        r = min(r, n-r)
        # 分子の計算
        numerator = factorial[n]
        # 分母の計算
        denominator = inverse[r] * inverse[n-r] % MODULUS
        return numerator * denominator % MODULUS

    res = 0
    for i in range(h-a):
        rights_and_downs_to_right_border_of_forbidden_area = i + (b-1)

        rights_and_downs_from_right_border_of_forbidden_area = (w - b - 1)  + (h - i - 1) 
        res = (res + ncr( rights_and_downs_to_right_border_of_forbidden_area,   b-1  ) \
            * ncr(  rights_and_downs_from_right_border_of_forbidden_area, (h - i - 1) )) % MODULUS


    print(res)