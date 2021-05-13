def main():
	H, W, A, B = map(int, input().split())
	H, W= H-1, W-1
	DIV = 10**9+7
	size = H+W+1

	fact = [0]*size
	inverse = [0]*size
	inv_cal = [0]*size
	fact[:2] = [1, 1]
	inverse[:2] = [1, 1]
	inv_cal[:2] = [0, 1]

	for i in range(2, size):
		fact[i] = (fact[i-1]*i%DIV)
		inv_cal[i] = (-inv_cal[DIV%i]*(DIV//i))%DIV
		inverse[i] = inverse[i-1]*inv_cal[i]%DIV

	def C(n, r):
		ans = fact[n]*inverse[r]%DIV
		return ans*inverse[n-r]%DIV

	ans = 0
	for x in range(B, W+1):
		y = H-A
		tmp = (C(x+y, x)*C(H+W-x-y-1, W-x))%DIV
		ans += tmp
		ans %= DIV

	print(ans)


if __name__ == '__main__':
	main()