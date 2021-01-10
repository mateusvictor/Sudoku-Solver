"""
Sudoku solver in Python 3.8 using backtracking.
By Mateus Victor.
"""

def solve(board):
	find = find_empty(board)

	if not find:
		return True
	else:
		row, col = find

	for i in range(1, 10):
		if valid(board, i, (row, col)):
			board[row][col] = i

			if solve(board):
				return True

			board[row][col] = 0

	return False

 
def valid(board, num, pos):
	"""Check if the a number is valid for the position 'pos'."""
	
	# Check row
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	# Check column
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	# Check box
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if board[i][j] == num and (i, j) != pos:
				return False

	return True

def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("---------------------")	

		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print("| ", end="")

			if j == 8:
				print(board[i][j])
			else:
				print(f"{board[i][j]} ", end="")

def find_empty(board):
	""" Returns the cordinates (row, column) of the first empty cell in the board """

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j)

	return None

sudoku_board = [
	[7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7],
]	
"""
sudoku_board = [
	[0, 0, 0, 0, 0, 0, 6, 8, 0],
	[0, 0, 0, 0, 7, 3, 0, 0, 9],
	[3, 0, 9, 0, 0, 0, 0, 4, 5],
	[4, 9, 0, 0, 0, 0, 0, 0, 0],
	[8, 0, 3, 0, 5, 0, 9, 0, 2],
	[0, 0, 0, 0, 0, 0, 0, 3, 6],
	[9, 6, 0, 0, 0, 0, 3, 0, 8],
	[7, 0, 0, 6, 8, 0, 0, 0, 0],
	[0, 2, 8, 0, 0, 0, 0, 0, 0],
]
"""

if __name__ == '__main__':
	print('Sudoku board: \n')
	print_board(sudoku_board)
	solve(sudoku_board)
	print('\n\nSudoku board solved:\n')
	print_board(sudoku_board)
