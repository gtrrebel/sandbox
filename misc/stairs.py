def poss(n, k, u, d):
	do = (d <= k)
	up = (u + k < n)
	return do, up

def next(n,k,u,d):
	do, up = poss(n,k,u,d)
	if do:
		return k - d
	elif up:
		return k + u
	else:
		return -1

def paint(n, u, d):
	i = 0
	l = [0 for _ in xrange(n)]
	k = 1
	while True:
		if i == n:
			break
		if l[i] == 0:
			run(l,i, k, u, d, n)
		k += 1
		i += 1
	return clean(l)


def run(l, i, k, u, d, n):
	while True:
		if i < 0:
			break
		l[i] = k
		i = next(n, i, u, d)

def clean(l):
	dic = {}
	i = 0
	col = 1
	while True:
		if i >= len(l):
			break
		if l[i] not in dic:
			dic[l[i]] = col
			col += 1
		l[i] = dic[l[i]]
		i += 1
	return l
