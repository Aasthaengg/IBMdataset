a, b = map(int, input().split())
p = "Positive"
print(p if 0<a else "Zero" if a<0<b else "Negative" if b<0 and -~(b-a)%2 else p)