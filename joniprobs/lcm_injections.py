import matplotlib.pyplot as plt
detailed_len = 15
simple_len = 3

def gcd(m,n):
	if m < n:
		return gcd(n,m)
	elif n < 0:
		return gcd(m, -n)
	elif n == 0:
		return m
	else:
		return gcd(n, m % n)

def lcm(*arg):
	if len(arg) <= 1:
		return sum(arg)
	else:
		a, b = arg[0], lcm(*arg[1:])
		if a == 0 or b == 0:
			return a + b
		else:
			return a*b/gcd(a,b)

def f(A, n):
	return lcm(*([n] + [n + i for i in A]))

def f_values(A, n):
	return [f(A, i) for i in xrange(1, n + 1)]

def plot_values(A, n):
	plt.figure()
	plt.plot(range(1, n + 1), f_values(A, n))
	plt.show()

def check(A, n):
	values = {}
	for i in range(1, n + 1):
		a = f(A, i)
		if a in values:
			return values[a], i
		else:
			values[a] = i
	return False

def check_all(k, n, detailed=True):
	if not detailed:
		print ' '*simple_len,
		for i in range(1, k + 1):
			print '{{0:{0}}}'.format(simple_len).format(i),
		print
	for i in xrange(1, k + 1):
		if not detailed:
			print '{{0:{0}}}'.format(simple_len).format(i),
		for j in xrange(1, k + 1):
			if j <= i:
				if detailed:
					print '-'*detailed_len,
				else:
					print '-'*simple_len,
			else:
				out = check([i, j], n)
				if detailed:
					if out:
						out = ' '.join([str(o) for o in out])
					else:
						out = ''
					print '{{0:{0}}}'.format(detailed_len).format(str(i) + ' ' + str(j) + ': ' + out),
				else:
					if out:
						out = str(out[0])
					else:
						out = ''*simple_len
					print '{{0:{0}}}'.format(simple_len).format(out),
		print

def ratio(k, n):
	count = 0
	for i in xrange(1, k + 1):
		for j in xrange(1, k + 1):
			if check([i, j], n):
				count += 1
	return count*1.0/(k*k)
