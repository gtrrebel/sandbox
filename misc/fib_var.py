
def fib(a,b,n):
	c = a + b
	while c % n == 0:
		c /= n
	return c

def seq(a, b, n):
	seq = [a, b, fib(a,b,n)]
	print a, b, seq[-1],
	while not check(seq, seq[-2], seq[-1]):
		seq.append(fib(seq[-2], seq[-1], n))
		print seq[-1],
	print

def seq_len(a, b, n):
	seq = [a, b, fib(a,b,n)]
	while not check(seq, seq[-2], seq[-1]):
		seq.append(fib(seq[-2], seq[-1], n))
	return len(seq) - check(seq, seq[-2], seq[-1]) - 2

def check(l, a, b):
	for i in xrange(len(l) - 2):
		if (a == l[i]) and (b == l[i + 1]):
			return i
	return False

k = 30
n = 3
seq(1,1,3)

for i in xrange(1, k + 1):
	for j in xrange(1, k + 1):
		print i, j, ": ",
		print seq_len(i,j,n)