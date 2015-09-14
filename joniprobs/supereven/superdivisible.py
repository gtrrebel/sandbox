import sys

if len(sys.argv) > 1:
	m = int(sys.argv[0])
	n = 100
	if len(sys.argv) > 2:
		n = int(sys.argv[1])
else:
	f = open("Users/otteheinavaara/Desktop/randomCodes/supereven/runstats.txt", 'r')
	now = f.readlines()[-1].split()
	if now[-1] == 'done':
		'calculation done\n' + \
		'host: ' + now[0] + '\n' + \
		'm = ' + now[1] + ', n = ' + now[2] + '\n' + \
		'last values:\n' + \
		now[3]
		'time used: ' + now[4]