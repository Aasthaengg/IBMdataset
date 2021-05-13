H, W, A, B = list(map(int, input().split()))
 
# 事前計算 + 演算ごとに mod する
def solve():
    # 組合せの計算用に階乗を事前計算しておく
    MOD = 10 ** 9 + 7
    FACT = [0] * (H + W + 1)
    INV_FACT = [0] * (H + W + 1)  # 逆元. 組合せの計算ごとにMODを取るため
 
    FACT[0], INV_FACT[0] = 1, 1
    for i in range(1, (H + W + 1)):
        FACT[i] = (FACT[i - 1] * i) % MOD
        INV_FACT[i] = pow(FACT[i], MOD - 2, MOD)  # フェルマーの小定理を使う
 
    def mod_nCr(n, r):
        if n < r or n == 0 or r == 0:
            return 1
 
        return FACT[n] * (INV_FACT[r] * INV_FACT[n - r]) % MOD
 
    # print(H, W, A, B)
 
    # 座標は(x, y). startは(0, 0)
    goal = W - 1, H - 1
 
    # 境界点: 移動できないエリアの右上の点
    nx = B - 1
    ny = H - A
 
    # 境界点から右斜め上に1つ移動した点(choke_left)から, 右端へ伸びる線がchoke points
    choke_left = nx + 1, ny - 1
 
    choke_points = []
    for i in range(B, W):
        choke_points.append((i, choke_left[1]))
 
    # 組合せを計算する: startからcp1, cp2からgoalまで組合せを掛ける
    ans = 0
    for cp1 in choke_points:
        x, y = cp1
        from_start_to_cp1 = mod_nCr(x + y, x)
 
        # cp1から1つ下の点がcp2
        y += 1
        dx, dy = goal[0] - x, goal[1] - y
        from_cp2_to_goal = mod_nCr(dx + dy, dx)
 
        ans = ans % MOD + (from_start_to_cp1 * from_cp2_to_goal % MOD) % MOD
 
    return ans % MOD
 
res = solve()
print(res)