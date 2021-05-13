def s():
	n, l, *a = map(int, open(0).read().split())
	for i, (x, y) in enumerate(zip(a, a[1:])):
		if x + y >= l:
			print("Possible")
			r = list(range(n))
			print("\n".join(map(str, r[1:i + 1] + r[n:i:-1])))
			break
	else:
		print("Impossible")
if __name__=="__main__":
	s()