import sys
from math import floor, sqrt, log
import pylab as pb

k = 1
m = 10
q = 1.5
i = 1

f = {}
f[0] = lambda N, n: N
f[1] = lambda N, n: log(N)/log(n)

if len(sys.argv) > 1:
	k = int(sys.argv[1])
	m = int(sys.argv[2])
	q = float(sys.argv[3])
	i = int(sys.argv[4])

def N(k,m,q):
	c = 0
	n = 1
	while c < k:
		if (int(floor(n**q)) % m) == 0:
			c += 1
		else:
			c == 0
		n += 1
	return n - k

def Ns(k, m, q):
	Ns = [0]*m
	c = 0
	n = 1
	while c < m - 1:
		a = int(floor(n**q))
		for i in xrange(1, m):
			if Ns[i] <= 0:
				if (a % (i + 1)) == 0:
					Ns[i] -= 1
					if Ns[i] == -k:
						Ns[i] = n - k + 1
						c += 1
				else:
					Ns[i] = 0
		n += 1
	return Ns[1:]

def plot_sks_Ns_f(a, m, q, i):
	k = len(a)
	xs = range(2, m + 1)
	for j in xrange(k):
		t = 1.0*j/k
		ys = [f[i](N, n) for N, n in zip(Ns(a[j], m, q), xs)]
		for x, y in zip(xs, ys):
			print x, y
		pb.plot(xs, ys, color=(sqrt(1- t), 0, 0))
	pb.show()

def plot_Ns(k, m, q):
	xs = range(1, m + 1)
	ys = Ns(k, m, q)
	pb.figure()
	pb.plot(xs,ys)
	pb.show()

def plot_sks_Ns(a, m, q):
	plot_sks_Ns_f(a, m, q, f[0])

def plot_ks_Ns(k, m, q):
	a = range(1, k + 1)
	plot_sKs_Ns(a, m, q)

def find_values(k, m, q):
	xs = range(2, m + 1)
	ys = [f[1](N, n) for N, n in zip(Ns(k, m, q), xs)]
	ysmax = [max(ys[i:]) for i in range(m - 1)]
	ysmin = [min(ys[i:]) for i in range(m - 1)]
	for x, y in zip(ysmin, ysmax):
		print x, y
	pb.plot(xs, ysmax)
	pb.plot(xs, ysmin)
	pb.show()

opt = 2
if opt == 0:
	a = range(1, k + 1)
elif opt == 1:
	a = [1,2,k]
else:
	a = [k]

plot_sks_Ns_f(a, m, q, i)
#find_values(k,m, q)

