from django.db import models
import json
BOARD_SIZE = 4
board =  [[['_' for _ in range(BOARD_SIZE)]  for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
NUM_CLIENTS = 3
turn = 1
winningPlayer = False
# Create your models here.
def checkWinningConditions(userId):
	global winningPlayer
	response = False
	if checkDiagonal(userId) == True or checkHorizontalAndMLVertical(userId) == True or checkVertical(userId) == True or checkMultiLevelDiagonal(userId) == True:
		response = True
		winningPlayer = int(userId)
	return response
def checkMultiLevelDiagonal(userId):
	global board
	response = False
	trueDiagonal1 = 0
	trueDiagonal2 = 0
	trueDiagonal3 = 0
	trueDiagonal4 = 0
	for i in range(BOARD_SIZE):
		topToBottom = 0
		bottomToTop = 0
		leftToRight = 0
		rightToLeft = 0
		rc1 = abs(i-(BOARD_SIZE-1)) #reversedCounter
		print()
		if str(board[int(i)][int(i)][int(i)]) == str(userId):
				trueDiagonal1 +=1
		if str(board[int(i)][int(rc1)][int(i)]) == str(userId):
				trueDiagonal2 +=1
		if str(board[int(rc1)][int(i)][int(i)]) == str(userId):
				trueDiagonal3 +=1
		if str(board[int(rc1)][int(rc1)][int(i)]) == str(userId):
				trueDiagonal4 +=1
		for j in range(BOARD_SIZE):
			rc = abs(j-(BOARD_SIZE-1)) #reversedCounter
			#topToBottom
			if str(board[int(j)][int(j)][int(i)]) == str(userId):
				topToBottom += 1
			#bottomToTop
			if str(board[int(j)][int(rc)][int(i)]) == str(userId):
				bottomToTop +=1
			#leftToRight
			if str(board[int(j)][int(i)][int(j)]) == str(userId):
				leftToRight +=1
			#rightToLeft
			if str(board[int(j)][int(i)][int(rc)]) == str(userId):
				rightToLeft +=1
			if topToBottom == BOARD_SIZE or bottomToTop == BOARD_SIZE or leftToRight==BOARD_SIZE or rightToLeft==BOARD_SIZE:
				response = True
		if trueDiagonal1 == BOARD_SIZE or trueDiagonal2 == BOARD_SIZE or trueDiagonal3 == BOARD_SIZE or trueDiagonal4 == BOARD_SIZE:
			response = True
	return response
def checkDiagonal(userId): #checks diagonal between levels
	global board
	winner = False
	for i in range(BOARD_SIZE):
		diag1 = 0
		diag2 = 0
		for j in range(BOARD_SIZE):
			rc1 = abs(j-(BOARD_SIZE-1)) 
			if str(board[int(i)][int(j)][int(j)]) == str(userId):
				diag1 += 1
			if str(board[int(i)][int(j)][int(rc1)]) == str(userId):
				diag2 += 1
		if diag2 ==BOARD_SIZE or diag1 == BOARD_SIZE:
			winner = True	
	return winner
def checkHorizontalAndMLVertical(userId): #ML = Multi-Level
	global board
	winner = False
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			lineCountHorizontal = 0
			lineCountMLVertical = 0
			for k in range(BOARD_SIZE):
				if str(board[i][j][k]) == str(userId):
					lineCountHorizontal += 1
				if str(board[k][j][i]) == str(userId):
					lineCountMLVertical += 1
			if lineCountHorizontal == BOARD_SIZE or lineCountMLVertical == BOARD_SIZE:
				winner = True
	return winner
def checkVertical(userId): #checks vertical between levels assuming the board is one flat surface. 
	global board 
	winner = False
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			for k in range(BOARD_SIZE):
				lineCount = 0
				for l in range(BOARD_SIZE):
					mid = j+l
					first = i
					if mid > BOARD_SIZE - 1:
						mid = abs(BOARD_SIZE-mid)
						first +=1
					if first < BOARD_SIZE and mid < BOARD_SIZE:
						if str(board[int(first)][int(mid)][int(k)]) == str(userId):
							lineCount += 1
				if lineCount == BOARD_SIZE:
					winner = True
	if lineCount == BOARD_SIZE:
		winner = True
	return winner
def showBoard(token):
    global board
    if int(token) > NUM_CLIENTS:
        data = False
    else:
        data = json.dumps(board)
    return data
def checkWinningPlayer():
    global winningPlayer
    return winningPlayer
def addToBoard(p1,p2,p3,id):
	global board
	global turn
	if board[p1][p2][p3] == '_':
		board[p1][p2][p3] = str(id)
		checkWinningConditions(id)
		turn += 1
		if turn > NUM_CLIENTS:
			turn = 1
		return True
	else:
		return False
def checkTurn(id):
	global turn
 #validates player turn
	if(int(id) == int(turn)):
		return True
	else:
		return False
def clearBoard():
	global board, winningPlayer
	board = [[['_' for _ in range(BOARD_SIZE)]  for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
	global turn
	turn = 1
	winningPlayer = False
	return 'O*'