import itertools
import numpy as np
import sys

N = int(sys.argv[1])
m = int(sys.argv[2])

def perm_value(perm, k):
	mak = 0
	n = len(perm)
	a = range(k)
	for i in range(n):
		mak = max(mak, sum([perm[(b + i) % n] for b in a]))
	return mak

def f(n, k):
	mik = n*k
	for a in itertools.permutations(range(1, n + 1)):
		mik = min(mik, perm_value(list(a), k))
	return mik


def printfs(n):
	for i in range(1, n + 1):
		for j in range(i):
			print f(i, j + 1),
		print

def printrandfs(n):
	for i in range(1, n + 1):
		for j in range(3, 4):
			print randf(i, j + 1),
		print

def randf(n,k):
	su = 0
	for i in range(m):
		su += perm_value(np.random.permutation(n), k)
	return (su*1./m + k)

#printrandfs(N)
print randf(N,2)