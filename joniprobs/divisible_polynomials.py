import sys

M = 100
n = 3
b = 2

if len(sys.argv) > 1:
	M, n, b = [int(i) for i in sys.argv[1:]]


def gcd(m,n):
	if m < n:
		return gcd(n,m)
	elif n < 0:
		return gcd(m, -n)
	elif n == 0:
		return m
	else:
		return gcd(n, m % n)

def pol_eval(C, x):
	s = 0
	for c in C:
		s = s*x + c
	return s

def coeff_gcd(C):
	if len(C) <= 1:
		return 0
	else:
		return gcd(coeff_gcd(C[1:]), C[0])

def pol_gcd(C, M):
	gd = 0
	for i1 in xrange(-M, M):
		for i2 in xrange(i1 + 1, M + 1):
			q = (pol_eval(C, i1) - pol_eval(C, i2))/(i1 - i2)
			gd = gcd(gd, q)
	return gd

def next_coeffs(n, b, C):
	if len(C) == 0:
		if n > 0:
			return [0]
		else:
			return ['end']
	if C[0] == b:
		return [0] + next_coeffs(n - 1, b, C[1:])
	else:
		return [C[0] + 1] + C[1:]

def pol_gcds(M, n, b):
	C = []
	m = 0
	while True:
		C = next_coeffs(n, b, C)
		if C[-1] == 'end':
			break
		r = level(C)
		if r and r > m:
			m = r
			print C, r

def level(C):
	a, b = pol_gcd(C, M), coeff_gcd(C)
	if a*b == 0:
		return False
	return a/b

pol_gcds(M, n, b)