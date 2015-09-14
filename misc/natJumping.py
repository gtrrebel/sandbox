import random
import math
from fractions import Fraction

k = 100
t = 10000

def jump(n):
	return n + random.randint(1, n)

def run(k):
	n = 1
	for i in range(k):
		n = jump(n)
	return n

def ave(k, t):
	count = 0
	for i in range(t):
		count += run(k)
	return count*1.0/t

def aves(k, t):
	return [ave(i,t) for i in range(1, k + 1)]

def paves(k, t, f= None):
	for i in range(1, k + 1):
		if f == None:
			print ave(i, t)
		else:
			print math.exp(f(ave(i,t))/i)

def recstep(M, k, n):
	ans = Fraction(0,1)
	for i in range((n+1)/2, n):
		ans += M[k-1][i]*Fraction(1, i)
	M[k][n] = ans

def makeTab(k):
	return makeTable((1 << (k - 1)), k)


def makeTable(n, k):
	M = [[Fraction(0,1) for i in range(n + 1)] for j in range(k + 1)]
	M[1][1] = Fraction(1,1)
	for i in range(2, k+1):
		for j in range(i, min(1 << i, n + 1)):
			recstep(M,i,j)
	return M

def printTab(M):
	k = len(M) - 1
	for i in range(1, k + 1):
		print i, ' ',
		for j in range(i, min((1 << (i - 1)) + 1, len(M[0]))):
			print j, ': ', M[i][j], ' ',
		print

def E(k):
	M = makeTab(k)
	e = []
	for i in range(1, k + 1):
		ex = 0
		for j in range(i, (1 << (i - 1)) + 1):
			ex += M[i][j]*Fraction(j,1)
		e.append(ex)
		print i, ': ', ex
	return e

E(10)