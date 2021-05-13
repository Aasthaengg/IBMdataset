S = input()

N_cnt = S.count('N')
W_cnt = S.count('W')
S_cnt = S.count('S')
E_cnt = S.count('E')

if ((N_cnt > 0 and S_cnt > 0) or (N_cnt == 0 and S_cnt == 0)) \
	and ((W_cnt > 0 and E_cnt > 0) or (W_cnt == 0 and E_cnt == 0)):
	print('Yes')
else:
	print('No')
