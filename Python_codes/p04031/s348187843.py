import statistics as st
import math
int(input())
s = list(map(int, input().split()))
md = math.floor(st.mean(s))
mu = md + 1
sd = 0
su = 0
for i in range(0, len(s)):
    sd = sd + (s[i] - md) ** 2
    su = su + (s[i] - mu) ** 2
print(min(sd, su))