moves = {}
winners = {}

class NC():

	def __init__(self, nc=None):
		if nc == None:
			self.board = [[0 for i in range(3)] for j in range(3)]
		else:
			self.board = [[i for i in row] for row in nc.board]

	def get_row(self, i):
		if i < 3:
			return zip([i]*3, range(3))
		elif i < 6:
			return zip(range(3), [i - 3]*3)
		elif i == 6:
			return zip(range(3), range(3))
		elif i == 7:
			return zip(range(3), range(3)[::-1])

	def put(self, place):
		self.board[place[0]][place[1]] = self.turn()

	def check_row(self, pairs):
		a = [self.board[i[0]][i[1]] for i in pairs]
		if all(i == 1 for i in a):
			return 1
		elif all(i == 2 for i in a):
			return 2
		return 0

	def set(self, *arg):
		self.board = [list(arg)[i:i+3] for i in xrange(0,9, 3)]

	def winner(self):
		for i in xrange(8):
			if self.check_row(self.get_row(i)) > 0:
				return self.check_row(self.get_row(i))
		return 0

	def paint(self, i):
		if i == 1:
			return 'x'
		elif i == 2:
			return 'o'
		else:
			return '_'

	def move(self):
		if self.hash() in moves:
			return moves[self.hash()]
		else:
			if self.winner() != 0:
				winners[self.hash()] = 3 - self.winner()
				moves[self.hash()] = 0
				return 0
			outcome = -1
			move = 0
			for i in xrange(3):
				for j in xrange(3):
					if self.board[i][j] == 0:
						child = NC(self)
						child.put((i, j))
						if outcome == -1 or outcome == 3 - self.turn():
							out = child.win()
							if out == 0:
								outcome = 0
							else:
								outcome = out
							move = (i, j)
						elif outcome == 0:
							out = child.win()
							if out == self.turn():
								outcome = out
								move = (i, j)
			moves[self.hash()] = move
			if move == 0:
				winners[self.hash()] = 0
			else:
				winners[self.hash()] = outcome
			return move

	def win(self):
		if self.hash() in winners:
			return winners[self.hash()]
		else:
			self.move()
			return self.win()

	def next(self):
		pair = self.move()
		next = NC(self)
		if pair != 0:
			next.put(pair)
		return next

	def game(self):
		print self
		print '\n'
		if self.move() != 0:
			self.next().game()

	def print_pos(self):
		for child in childs:
			print child, '\n'

	def childs(self):
		t = self.turn()
		childs = []
		for i in xrange(3):
			for j in xrange(3):
				if self.board[i][j] == 0:
					childs.append(NC(self))
					childs[-1].put((i, j))
		return childs

	def turn(self):
		ones, twos = 0, 0
		for i in xrange(3):
			for j in xrange(3):
				a = self.board[i][j]
				if a == 1:
					ones += 1
				elif a == 2:
					twos += 1
		if ones == twos:
			return 1
		else:
			return 2

	def hash(self):
		return sum((27**i)*sum((3**j)*self.board[i][j] for j in xrange(3)) for i in xrange(3))


	def __str__(self):
		return '\n'.join([' '.join([self.paint(i) for i in row]) for row in self.board])
