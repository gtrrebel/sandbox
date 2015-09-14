import sys

n = 10

if len(sys.argv) > 1:
	n = int(sys.argv[1])

def integer_part_root(n, k):
	ala, yla = 1, 1
	while yla**k < n:
		yla *= 2
	ala = yla/2
	while True:
		keski = (ala+yla)/2
		power = keski**k
		if power > n:
			yla = keski
		elif power < n:
			ala = keski
		else:
			return keski
		if ala + 1 >= yla:
			break;
	if yla**k > n:
		return ala
	else:
		return yla

def check(n, k):
	return (integer_part_root(n,k) % 2) == 0

def N(a, k):
	n = 1
	while True:
		if check(a**n, k):
			return n
		n += 1

def next(a, k):
	n = N(a, k)
	a = integer_part_root(a**n, k) + 1
	return a, n

def thresholds(M, a=None, n=None):
	if a == None or n == None:
		a, n = 3, 2
	for i in xrange(M):
		a, n = next(a, n)
		print a, n, a**(1./n)

def threshold_continue(M):
	f = open('supereven.txt', 'r+')
	a, n = [int(i) for i in f.readlines()[-1].split()[:2]]
	for i in xrange(M):
		a, n = next(a, n)
		f.write(str(a) + ' ' + str(n) +' ' + str(a**(1./n)) + '\n')
		print a, n, a**(1./n)
	f.close()
	

threshold_continue(n)