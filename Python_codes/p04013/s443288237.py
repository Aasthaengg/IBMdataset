import sys
def input(): return sys.stdin.readline().strip()
offset = 2500

def main():
    N, A = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(N): X[i] -= A
    dp = [0] * 5010
    dp[offset] += 1
    dp[X[0] + offset] += 1
    for i, x in enumerate(X):
        if i == 0: continue
        dp2 = [0] * 5010
        for j in range(5010):
            if j < x or j - x >= 5010:
                dp2[j] = dp[j]
            else:
                dp2[j] = dp[j] + dp[j - x]
        dp = dp2
        #print(dp[offset - 3: offset + 4])
    print(dp[offset] - 1)

if __name__ == "__main__":
    main()
