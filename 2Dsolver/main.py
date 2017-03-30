def solver(matrix, patterns):
	print matrix
	print pattern
	d = dict()
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[0])):
			for k in xrange(len(patterns)):
				if matrix[i][j] == -1:
					continue
				if ok(matrix, patterns[k], i, j):
					if matrix[i][j] in d:
						if k in d[matrix[i][j]]:
							d[matrix[i][j]][k] += 1
						else:
							d[matrix[i][j]][k] = 1
					else:
						i_d = dict()
						i_d[k] = 1
						d[matrix[i][j]] = i_d
					for ii in xrange(0, patterns[k][0]):
						for jj in xrange(0, patterns[k][1]):
							matrix[i+ii][j+jj] = -1
	print d

def ok(matrix, pattern, x, y):
	base = matrix[x][y]
	for i in xrange(0, pattern[0]):
		for j in xrange(0, pattern[1]):
			if x+i >= len(matrix) or y+j >= len(matrix[0]):
				return False
			if matrix[x+i][y+j] != base:
				return False
	return True

matrix = [
	[0,1,0,0],
	[0,1,1,1],
	[1,1,1,0],
	[0,0,1,0]
]
pattern = [
	[2,2],
	[2,1],
	[1,2],
	[1,1]
]

solver(matrix, pattern)
