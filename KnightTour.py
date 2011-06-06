# Knight's Tour
# Author: Matt Hammond 
# Some python syntax borrowed fromt the internet where noted
# Produces an 8x8 grid demonstrating a knight's tour of an 8x8 chessboard, always starting from 
# the bottom rightmost position. Utilizes the Warnsdorff heuristic (see Wikipedia).
# Runs until a tour is found, so it could technically run forever, but it is extemely likely
# a solution will be found within 2 iterations of the algorithm.
# There are probably a number of more elegant shotcuts I could've used in this program, like mapping
# functions, recursion, etc. I also could've used a dictionary indexed with tuples instead of this 
# C-wannabe 2-D array made of lists, but the immutability of tuples can be a headache, and it's been a
# while since I've used Python. Also, I'm knee deep in finals right now, so ELEGANCE MUST WAIT!
import random
# In the interest of full disclosure, stole this 2-D array (List of lists in Python) 
# initialization from an internet forum.
Board = [[0 for col in range(8)] for row in range(8)]
CurrentPosition = (7,6)
MoveCount = 1

# Function that takes a position in the form of a tuple of the form (row, column) indexed 0-7,
# starting in the top left, and returns a list of tuples representing the available positions
# reachable in one move from the starting position. Checks the available 8 moves and makes sure
# they're within the 8x8 grid, and that the position hasn't already been visited.
def nextMoves(Position):
	Moves = []
	if(Position[0] + 2 < 8 and Position[1] + 1 < 8 and Board[Position[0]+2][Position[1]+1] == 0):
		Moves.append((Position[0]+2,Position[1]+1))
	if(Position[0] + 2 < 8 and Position[1] - 1 >= 0 and Board[Position[0]+2][Position[1]-1] == 0):
		Moves.append((Position[0]+2,Position[1]-1))
	if(Position[0] - 2 >= 0 and Position[1] + 1 < 8 and Board[Position[0]-2][Position[1]+1] == 0):
		Moves.append((Position[0]-2,Position[1]+1))
	if(Position[0] - 2 >= 0 and Position[1] - 1 >= 0 and Board[Position[0]-2][Position[1]-1] == 0):
		Moves.append((Position[0]-2,Position[1]-1))
	if(Position[0] + 1 < 8 and Position[1] + 2 < 8 and Board[Position[0]+1][Position[1]+2] == 0):
		Moves.append((Position[0]+1,Position[1]+2))
	if(Position[0] - 1 >= 0 and Position[1] + 2 < 8 and Board[Position[0]-1][Position[1]+2] == 0):
		Moves.append((Position[0]-1,Position[1]+2))
	if(Position[0] + 1 < 8 and Position[1] - 2 >= 0 and Board[Position[0]+1][Position[1]-2] == 0):
		Moves.append((Position[0]+1,Position[1]-2))
	if(Position[0] - 1 >= 0 and Position[1] - 2 >= 0 and Board[Position[0]-1][Position[1]-2] == 0):
		Moves.append((Position[0]-1,Position[1]-2))
	return Moves

# Function that implements the Warnsdorff heauristic, checking each primary move available from the 
# provided position (once again a tuple), and choosing the secondary move with the least available moves.
# In the event of a tie in the number of secondary moves available to the primary moves, a random
# primary move is returned. This function returns a position in the form of a tuple.
def chooseNext(Position):
	Possible = []
	Low = 9
	for move in nextMoves(Position):
		if (len(nextMoves(move)) == Low):
			Possible.append(move)
		elif (len(nextMoves(move)) < Low):
			Possible = [move]
			Low = len(nextMoves(move))
	if (len(Possible) != 0):
		return random.choice(Possible)
	else: return None

# This is the main loop of the program, iterating through moves until their are no moves left. If a
# complete tour is not found, the board is reset and the loop starts over until a tour is found.
while (MoveCount < 65):
	if (CurrentPosition == None):
		Board = [[0 for col in range(8)] for row in range(8)]
		CurrentPosition = (7,6)
		MoveCount = 1
	Board[CurrentPosition[0]][CurrentPosition[1]] = MoveCount
	CurrentPosition = chooseNext(CurrentPosition)
	MoveCount = MoveCount + 1

# This displays the board, and was stolen from the same forum as the piece initializing the 2-D array
for row in Board:
	print row