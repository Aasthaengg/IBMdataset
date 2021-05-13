def frac_with_mod(a,m):
    outlist = [ 1 for i in range(a+1) ]
    for i in range(1,a+1):
        outlist[i] = (outlist[i-1] * i)% m
    return outlist

frac_list = frac_with_mod(2*10**5,10**9+7)

def comb_with_mod(a,b,m):
    global frac_list
    return ( frac_list[a+b-2] * pow(frac_list[a-1],m-2,m) * pow(frac_list[b-1],m-2,m) ) % m

mod = 10**9+7
h, w, a, b = [ int(v) for v in input().split() ]

c = h - a
d = w - b


if c == 1:
    waypoint_list = [ 1 for i in range(d) ]
else:
    waypoint_list = [ comb_with_mod(b+1+i,c-1,mod) for i in range(d) ]
    s = comb_with_mod(b,c,mod)

    for i in range(d):
        waypoint_list[i] = ( s + waypoint_list[i] ) % mod
        s = waypoint_list[i]
        waypoint_list[i] = ( comb_with_mod(a,d-i,mod) * waypoint_list[i] ) % mod

print(sum(waypoint_list)%mod)