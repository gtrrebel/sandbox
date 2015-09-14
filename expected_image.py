import sys
from fractions import Fraction

if len(sys.argv) > 1:
	n = int(sys.argv[1])
else:
	n = 3
expects = {}

def expect(n):
	return expected(n, 0, 0)

def expected(n, k, a):
	global expects
	if (n, k, a) in expects:
		pass
	elif k == n:
		expects[(n, k, a)] = Fraction(a,1)
	else:
		expects[(n, k, a)] = expected(n, k + 1, a)*Fraction(a, n) + expected(n, k + 1, a + 1)*Fraction(n - a, n)
	return expects[(n, k, a)]

print expect(n)
