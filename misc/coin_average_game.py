import sys
from fractions import Fraction

n = 3

if len(sys.argv) > 1:
	n = int(sys.argv[1])

expects = {}

def E(n,a,b):
	global expects
	if (n,a,b) in expects:
		return expects[(n,a,b)]
	if a + b == n:
		expects[(n,a,b)] = Fraction(a, n)
	else:
		if a + b > 0:
			expects[(n,a,b)] = max(Fraction(1,2)*E(n,a+1,b)+Fraction(1,2)*E(n,a,b+1), Fraction(a,a+b))
		else:
			expects[(n,a,b)] = Fraction(1,2)*E(n,a+1,b)+Fraction(1,2)*E(n,a,b+1)
	return expects[(n,a,b)]

for i in xrange(1, n + 1):
	q = E(i, 0, 0)
	print q, float(q)