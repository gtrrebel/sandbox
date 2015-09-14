import sys
from math import floor, sqrt, log
import pylab as pb

n = 5

f = {}
f[0] = lambda N, n: N

if len(sys.argv) > 1:
	n = int(sys.argv[1])

def N2(q, m):
	n = 1
	while True:
		if (int(floor(q**n)) % m) == 0:
			return n
		n += 1

def N2s(k, m, q):
	N2s = [0]*m
	c = 0
	n = 1
	while c < m - 1:
		a = int(floor(q**n))
		for i in xrange(1, m):
			if N2s[i] <= 0:
				if (a % (i + 1)) == 0:
					N2s[i] -= 1
					if N2s[i] == -k:
						N2s[i] = n - k + 1
						c += 1
				else:
					N2s[i] = 0
		n += 1
	return N2s[1:]

def plot_sks_N2s_f(a, m, q, i):
	k = len(a)
	xs = range(2, m + 1)
	for j in xrange(k):
		t = 1.0*j/k
		ys = [f[i](N, n) for N, n in zip(N2s(a[j], m, q), xs)]
		for x, y in zip(xs, ys):
			print x, y
		pb.plot(xs, ys, color=(sqrt(1- t), 0, 0))
	pb.show()

def plot_N2s(k, m, q):
	xs = range(1, m + 1)
	ys = N2s(k, m, q)
	pb.figure()
	pb.plot(xs,ys)
	pb.show()

def plot_sks_N2s(a, m, q):
	plot_sks_N2s_f(a, m, q, f[0])

def plot_ks_Ns(k, m, q):
	a = range(1, k + 1)
	plot_sKs_N2s(a, m, q)

def find_values(k, m, q):
	xs = range(2, m + 1)
	ys = [f[1](N, n) for N, n in zip(N2s(k, m, q), xs)]
	ysmax = [max(ys[i:]) for i in xrange(m - 1)]
	ysmin = [min(ys[i:]) for i in xrange(m - 1)]
	for x, y in zip(ysmin, ysmax):
		print x, y
	pb.plot(xs, ysmax)
	pb.plot(xs, ysmin)
	pb.show()

def max_parity_value(n):
	ma = 0
	for i in xrange(1, n + 1):
		for j in xrange(1, n + 1):
			if ((i % j) != 0) and (i > j) and (i*i > 2*j*j):
				ma = max(N2(i*1./j, 2), ma)
	print ma

def parity_values(n):
	for i in xrange(1, n + 1):
		for j in xrange(1, n + 1):
			if ((i % j) != 0) and (i > j):
				print '{0:3}'.format(str(N2(i*1./j, 2))),
			else:
				print '{0:3}'.format('-'),
		print

def parity_values_m(n, m):
	for i in xrange(1, n + 1):
		if ((i % m) != 0):
			print N2(i*1./m, 2),
	print

def plot_parity_values_m(n, m):
	xs = []
	ys = []
	for i in xrange(1, n + 1):
		if ((i % m) != 0):
			ys.append(N2(i*1./m, 2))
			xs.append(i)
	pb.figure()
	pb.plot(xs, ys, 'ro')
	pb.show()

def next_thresholds(a, n):
	q = a**(1./n)
	n = N2(q, 2)
	print n
	a = int(floor(q**n))
	return a + 1, n

def thresholds(a, n, b):
	q = a**(1.0/n)
	while q < b:
		print q, a, n
		a, n = next_thresholds(a, n)
		q = a**(1.0/n)
		break

def test1(k,m,q, i):
	opt = 2
	if opt == 0:
		a = range(1, k + 1)
	elif opt == 1:
		a = [1,2,k]
	else:
		a = [k]

	plot_sks_N2s_f(a, m, q, i)
	#find_values(k,m, q)

def test2(n):
	parity_values(n)

def test3(n):
	max_parity_value(n)

def test4(n, m):
	plot_parity_values_m(n, m)

test4(n, 3)

