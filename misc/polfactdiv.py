import sys
from fractions import Fraction

n = 3
k = 5

if len(sys.argv) > 1:
	n = int(sys.argv[1])

if len(sys.argv) > 2:
	k = int(sys.argv[2])

def ratio(n, k):
	small, big = n, n
	for i in xrange(1, k + 1):
		big *= small
		small *= small - 1
	return Fraction(small,big)

def print_ratios(n, k):
	small, big = n, n
	for i in xrange(1, k + 1):
		big *= small
		small *= small - 1
		print float(Fraction(small,big))

print_ratios(n, k)