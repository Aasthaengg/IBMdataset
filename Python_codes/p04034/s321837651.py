#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N, M = map(int, input().split())
    dp = {1:[1,True]}         #dp[i]  iの箱の状態　[x個]赤がいる可能性がある
    for _ in range(2,N+1):
        dp[_] = [1,False]
    for _ in range(M):
        fm, to = map(int, input().split())
        num, state = dp[fm]
        #fmの処理
        dp[fm][0]-=1    #移動
        if dp[fm][0]==0:
            dp[fm][1] = False
        #toの処理
        dp[to][0]+=1    #移動
        dp[to][1]=dp[to][1] or state
    ret = 0
    for _ in range(1,N+1):
        ret += dp[_][1]
    print(ret)

if __name__ == '__main__':
    main()