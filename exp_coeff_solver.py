import numpy as np

def ab_coeff(a,b):
	l = np.zeros((a+b+1))
	l[0] = 1
	l[-1] = 1
	l[b] = -2
	return coeff_coeff(*l)

def coeff_coeff(*arg):
	return root_coeff(*np.roots(arg))

def root_coeff(*arg):
	return np.linalg.inv(vanmatrix(arg))

def mult(a):
	b = {}
	for i in a:
		if i not in b:
			b[i] = 1
		else:
			b[i] = b[i] + 1
	return b

def vanmatrix(a):
	n = len(a)
	b = mult(a)
	A = np.zeros((n,n))
	r = 0
	for i in b:
		for j in xrange(b[i]):
			for k in xrange(n):
				A[r][k] = (k**j)*(i**(k))
			r += 1
	return A
