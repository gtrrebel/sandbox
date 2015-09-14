import random
import itertools

def value(part):
	return sum(abs(sum(box) - 1) for box in part)

def partition(l):
	part = []
	for i in l:
		if len(part) == 0:
			part.append([i])
		elif sum(part[-1]) + i < 1:
			part[-1].append(i)
		else:
			r = random.randint(0,1)
			if r == 1:
				part[-1].append(i)
			else:
				part.append([i])
	return part

def discrepancy(l):
	return min(division(list(perm)) for perm in itertools.permutations(l))

def division(l):
	if l:
		return min(abs(sum(l[:i]) - 1) + division(l[i:]) for i in xrange(1, len(l) + 1))
	else:
		return 0

def discrepancy_approx(l, M):
	best = len(l)
	for _ in xrange(M):
		random.shuffle(l)
		best = min(best, value(partition(l)))
	return best

def D(n, N):
	return sum(discrepancy([random.uniform(0,1) for i in xrange(n)]) for j in xrange(N))/N

def D2(n, N):
	s = 0
	for j in xrange(1, N + 1):
		s += discrepancy([random.uniform(0,1) for i in xrange(n)])
		print s/j

