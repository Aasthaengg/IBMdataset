# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:28:00 2020

@author: NEC-PCuser
"""

N, M = map(int, input().split())
x, y = [], []

for i in range(M):
    x_tmp, y_tmp = map(int, input().split())
    x.append(x_tmp)
    y.append(y_tmp)

box = [1] * N 
ball_set = set()
ball_set.add(1)
start_flg = True
for i in range(len(x)):
    if x[i] in ball_set:
        ball_set.add(y[i])
    box[x[i] - 1] -= 1
    box[y[i] - 1] += 1
    if box[x[i] - 1] == 0:
        ball_set.discard(x[i])

print(len(ball_set))

