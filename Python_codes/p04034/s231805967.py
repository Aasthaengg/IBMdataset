# AGC002 B Box and Ball

n, m = map(int, input().split())

b_list = [0] * (n+1)
b_list[1] = 1
c_list = [1] * (n+1)

for i in range(m):
    _x, _y = map(int, input().split())
    c_list[_x] -= 1
    c_list[_y] += 1 
    if b_list[_x] == 1:
        b_list[_y] = 1
        if c_list[_x] == 0:
            b_list[_x] = 0

print(sum(b_list))