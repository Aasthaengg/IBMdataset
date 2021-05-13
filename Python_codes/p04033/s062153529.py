def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

a,b = i2()
if a > 0:
	print("Positive")
elif a <= 0 and 0 <= b:
	print("Zero")
else:
	if (b - a)%2 == 0:
		print("Negative")
	else:
		print("Positive")