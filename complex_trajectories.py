import sys
import cmath
import pylab as pb
from numpy import pi
from cmath import exp
from math import sqrt

upcoeffs = [(3, pi/3), (4 + 5j, pi/5)]
downcoeffs = [(2 + 3j, pi/3), (-1-7j, pi/5)]
roots = [1, exp(1j), exp(2*1j), exp(3*1j)]
coeffs = [1, 2, 4, 8]

n = 10000
if len(sys.argv) > 1:
	n = int(sys.argv[1])

def b(n, roots, coeffs):
	up, down = 0, 0
	for r, c in zip(roots, coeffs):
		up += c*(r/roots[0])**(n + 1)
		down += c*(r/roots[0])**(n)
	return up/down

def f(x, upcoeffs, downcoeffs):
	up = 1 + 0j
	for upcoeff in upcoeffs:
		up += upcoeff[0]*cmath.exp(((x*upcoeff[1]))*1j)
	down = 1 + 0j
	for downcoeff in downcoeffs:
		down += downcoeff[0]*cmath.exp((x*downcoeff[1])*1j)
	return up/down

def plot_discrete_trail(a, b, upcoeffs, downcoeffs):
	l = [f(k, upcoeffs, downcoeffs) for k in xrange(a, b + 1)]
	re = [n.real for n in l]
	im = [n.imag for n in l]
	pb.figure()
	pb.plot(re, im, 'bo', label='sampled')
	pb.show()

def plot_continuous_trail(a, b, n, upcoeffs, downcoeffs):
	l = [f(a*1. + k*(b-a)*1./n, upcoeffs, downcoeffs) for k in xrange(n + 1)]
	re = [n.real for n in l]
	im = [n.imag for n in l]
	pb.figure()
	pb.plot(re, im, 'bo', label='sampled')
	pb.show()

def plot_bs(n, roots, coeffs):
	l = [b(k, roots, coeffs) for k in xrange(n + 1)]
	re = [n.real for n in l]
	im = [n.imag for n in l]
	pb.figure()
	pb.plot(re, im, 'bo', label='sampled')
	pb.show()

plot_bs(n, roots, coeffs)
