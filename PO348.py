def is_square(n):
	if n == 1:
		return True
	x = n // 2
	seen = set([x])
	while x * x != n:
		x = (x + (n // x)) // 2
		if x in seen:
			return False
		seen.add(x)
	return True

def check(n):
	k = 1
	b = n**(1./3)
	ways = 0
	while k <= b:
		if is_square(n - k*k*k):
			ways += 1
			if ways > 4:
				return False
		k += 1
	return ways == 4

nums = []
n = 1
odd = True

def check_power_ten(n):
	if n == 0:
		return False
	elif n == 1:
		return True
	else:
		return check_power_ten(n // 10) & ((n % 10) == 0)

def next_pair(n, odd):
	n += 1
	if check_power_ten(n):
		if odd:
			odd = False
			n = n // 10
		else:
			odd = True
	return n, odd

def turn(n, odd):
	if odd:
		return int(str(n) + str(n)[-2::-1])
	else:
		return int(str(n) + str(n)[-1::-1])

def main():
	n, odd = 1, True
	while len(nums) < 5:
		n, odd = next_pair(n, odd)
		if check(turn(n, odd)):
			nums.append(turn(n, odd))
			print turn(n, odd)

main()