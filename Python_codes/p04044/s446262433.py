#!/usr/bin/env python3
_, _, *s = open(0).read().split()
s.sort()
print(*s, sep="")
