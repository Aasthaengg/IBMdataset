# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys

def s():
    return raw_input().strip()
def n():
    return int(raw_input())
def d():
    return float(raw_input())

def ls():
    return raw_input().strip().split()
def ln():
    return map(int, raw_input().strip().split())
def ld():
    return map(float, raw_input().strip().split())

def fs():
    return [raw_input().strip() for i in xrange(input())]
def fn():
    return [int(raw_input().strip()) for i in xrange(input())]
def fd():
    return [float(raw_input().strip()) for i in xrange(input())]

N, L = ln()

A = ln()

candidate = -1

for i in xrange(N - 1):
    if A[i] + A[i + 1] >= L:
        candidate = i

if candidate != -1:
    print 'Possible'
    for i in xrange(candidate):
        print i + 1
    for i in xrange(N - 1, candidate, -1):
        print i
else:
    print 'Impossible'
