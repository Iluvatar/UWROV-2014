import random
import time

print 'Note: Maximize window for best effect'
sizeStr = raw_input('Choose the size between 5 and 40: ')
size = int(sizeStr)
timerStr = raw_input('Choose the time between gens between 0.2 and 1: ')
timer = float(timerStr)

def start():
	small = []
	large = []
	for i in range(size):
		for j in range(size):
			small.append(random.randint(0, 1))
		large.append(small)
		small = []
	return large

def drawBoard(board):
	for i in range(size):
		line = ""
		for j in range(size):
			if board[i][j] == 1:
				line = line + "@ "
			else:
				line = line + "  "
		print line

def nextGen(board):
	small = []
	large = []
	for y in range(size):
		for x in range(size):
			if x == 0:
				xl = size - 1
			else:
				xl = x - 1
			if x == size - 1:
				xr = 0
			else:
				xr = x + 1
			if y == 0:
				yu = size - 1
			else:
				yu = y - 1
			if y == size - 1:
				yd = 0
			else:
				yd = y + 1
			add = board[yu][xl] + board[yu][x] + board[yu][xr] + board[y][xl] + board[y][xr] + board[yd][xl] + board[yd][x] + board[yd][xr]
			if add == 3:
				small.append(1)
			elif add == 2:
				if board[y][x] == 0:
					small.append(0)
				else:
					small.append(1)
			else:
				small.append(0)
		large.append(small)
		small = []
	return large



board = start()
while True:
	drawBoard(board)
	for a in range(60 - size):
		print
	board = nextGen(board)
	time.sleep(timer)