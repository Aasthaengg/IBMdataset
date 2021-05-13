(N, M), *AB = [map(int, s.split()) for s in open(0)]
cnt = [1] * N
possibly_red = [False] * N
possibly_red[0] = True
for a, b in AB:
    a -= 1
    b -= 1
    cnt[a] -= 1
    cnt[b] += 1
    if possibly_red[a]:
        possibly_red[b] = True
        if cnt[a] == 0:
            possibly_red[a] = False
print(sum(possibly_red))
