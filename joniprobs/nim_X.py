
def value(values, X):
	return - min([values[-i] for i in X])

def values(X, N):
	X = sorted(X)
	if X:
		vals = values(X[:-1], X[-1] - 1)
		for i in xrange(X[-1], N + 1):
			vals.append(value(vals, X))
	else:
		vals = [-1]
		for i in xrange(1, N + 1):
			vals.append(0)
	return vals

def value_guess(X, n):
	b = max(X)
	a = min(X)
	if n <= b:
		return True
	else:
		r = (n - b + a - 1) % (a + b)
		q = r/a
		return (q % 2) == 0

def solution_guess(X, N):
	values = [False]
	for i in xrange(1, N + 1):
		values.append(value_guess(X, i))
	return values

def values_p(X, N):
	vals = values(X, N)
	for i in xrange(N + 1):
		print paint(vals[i]),
	print

def paint(i):
	if i == 0:
		return '_'
	elif i == -1:
		return ' '
	elif i == 1:
		return '*'

def print_X_values(X, m):
	print_values(values(X, m))

def print_values(V):
	for v in V:
		if v:
			print 1,
		else:
			print 0,
	print

def vs(V1, V2):
	C = [not i1 ^ i2 for i1, i2 in zip(V1, V2)]
	return all(C)

def check_X(X, m):
	return vs(values(X, n), solution_guess(X, n))

def values_ab(a,b,n):
	vals = values([a,b], n)
	for i in xrange(n + 1):
		print paint(vals[i]),
		if (i + 1) % (a+b) == 0:
			print
	print

def check(n, m):
	mat = []
	for i1 in xrange(1, n + 1):
		row = []
		for i2 in xrange(1, n + 1):
			row.append(check_X([i1,i2], m))
		mat.append(row)
	return all(all(row) for row in mat)
