from sys import stdin, stdout
from itertools import repeat
def main():
    n, l = map(int, stdin.readline().split())
    a = map(int, stdin.read().split(), repeat(10, n))
    for i in xrange(n - 1):
	if a[i] + a[i+1] >= l:
            ans = range(1, i + 1) + range(n - 1, i + 1, -1) + [i + 1]
            stdout.write('Possible\n')
            stdout.write('\n'.join(map(str, ans)))
            stdout.write('\n')
            return
    print "Impossible"
main()
