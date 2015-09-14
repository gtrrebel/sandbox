import pylab as pb


def plot_supereven(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	xs = range(len(lines))
	ys = [line.split()[1] for line in lines]
	pb.figure()
	pb.plot(xs, ys)
	pb.show()
	f.close()

def plot_supereven2(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	xs = range(len(lines))
	ys = [line.split()[2] for line in lines]
	pb.figure()
	pb.plot(xs, ys)
	pb.show()
	f.close()

plot_supereven('superevensave2.txt')
