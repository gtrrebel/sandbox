import sys
import matplotlib.pyplot as plt

b = 3
n = 3
m = 2

if len(sys.argv) > 1:
	b, n, m = [int(i) for i in sys.argv[1:]]

def plot_intervals(b, n, m):
	for i in xrange(1, n + 1):
		j = 0
		c = b**i
		while True:
			if j*m + 1 > c:
				break
			plt.hlines(i, (j*m)**(1.0/i), (j*m + 1)**(1.0/i), lw=4)
			j += 1
	plt.ylim(0,n + 1)
	plt.show()

plot_intervals(b, n, m)