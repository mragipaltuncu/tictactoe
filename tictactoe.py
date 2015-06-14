import os
import platform
import time

#Main list to represent the game board
board = [""," "," "," "," "," "," "," "," "," "]

#Self exlanatory, prints welcome_msg
def welcome_header():
	welcome_msg = (r"""

████████╗██╗ ██████╗████████╗ █████╗  ██████╗████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔════╝    1|2|3
   ██║   ██║██║        ██║   ███████║██║        ██║   ██║   ██║█████╗  	   4|5|6
   ██║   ██║██║        ██║   ██╔══██║██║        ██║   ██║   ██║██╔══╝  	   7|8|9
   ██║   ██║╚██████╗   ██║   ██║  ██║╚██████╗   ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
                                                                       

//Welcome Friend! Place X to a desired location on the grid.
//Boxes on the grid are numbered from 1 to 9. 
//To win you must have three X either horizontally or diagonally placed.
//Good luck!
""")

	print(welcome_msg)

#The main header on top. Keeps clearing the command line for better view.
#if argument 'end' is passed to the function it prints out a goodbye header.
def game_header(state='begin'):
	if state == 'begin':
		commands = {"Linux" : "clear", "Windows" : "cls", "Darwin" : "clear"}
		os.system(commands[platform.system()])
		welcome_header()
		draw_board()
	elif state == 'end':
		commands = {"Linux" : "clear", "Windows" : "cls", "Darwin" : "clear"}
		os.system(commands[platform.system()])
		goodbye_header()

#Takes board list and prints in in a nice format.
def draw_board(board=board):
	print('\n')
	print('|',board[1],'|',board[2],'|',board[3],'|')
	print('-------------')
	print('|',board[4],'|',board[5],'|',board[6],'|')
	print('-------------')
	print('|',board[7],'|',board[8],'|',board[9],'|')
	print('\n')	  

#Takes player('X' or 'O') and the game board.
#Defines all possible win condition positions.
#Goes through all sets of conditions and checks if all 3 positions are the same player('X' or 'O')
#If all 3 winning condition positions are same player's returns True.
def is_winner(player,board=board):
	win_conditions = [#Horizontal
					  [1,2,3],[4,5,6],[7,8,9],
					  #Vertical
					  [1,4,7],[2,5,8],[3,6,9],
					  #Diagonal
					  [1,5,9],[3,5,7]
					 ]
	for condition in win_conditions:
		count = 0
		for position in condition:
			if board[position] == player:
				count += 1
			
			if count == 3:
				return True
	return False

#Checks for a tie situation. If there's no empty string (" ") left in board list returns True
def is_tie(board=board):
	if " " not in board:
		return True

#Takes player('X' or 'O') and board as arguments. First checks for a winner if there's a winner returns True
#Then checks for a tie situation. 
#If both checks fail returns False
def check_winner_tie(player,board=board):
	if is_winner(player):
		print("Player {} wins!".format(player))
		return True
	elif is_tie():
		print("It's a tie")
		return True
	else:
		return False

#Takes player('X' or 'O') and board as arguments.
#Ask player for input. Depending on player argument ('X' or 'O') it formats the input question string.
#After getting the board position from the player, changes that position in board list to player's sign ('X' or 'O')
def get_player_input(player, board=board):
	player_input = int(input("{}Choose a box to put {} [1-9] : ".format("Player1 -- " if player == 'X' else "Player2 -- ",player)))
	board[player_input] = player

#Asks player for a rematch
#If yes, it refreshes the board and calls the main() function to startover the game
#Otherwise it prints the game_header() function with 'end' argument to output goodbye_header()
def rematch(board=board):
	
	ask_rematch = input("Play again? [Y/N]")
	ask_rematch = ask_rematch.lower()
	if ask_rematch in ['y','yes']:
		print("A new challegen begins!")
		time.sleep(1)
		refresh_board()
		main()
		
	else:
		print ("Thank you for playing!")
		refresh_board()
		game_header('end')

#A simple function to clear the main game board list for a new game.
def refresh_board(board=board):
	for i in range(1,len(board)):
		board[i] = " "

#Like welcome_header, this header is to be displayed when a game ends and the player does not want a rematch.
def goodbye_header():
	goodbye_msg = (r"""

████████╗██╗ ██████╗████████╗ █████╗  ██████╗████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔════╝    1|2|3
   ██║   ██║██║        ██║   ███████║██║        ██║   ██║   ██║█████╗  	   4|5|6
   ██║   ██║██║        ██║   ██╔══██║██║        ██║   ██║   ██║██╔══╝  	   7|8|9
   ██║   ██║╚██████╗   ██║   ██║  ██║╚██████╗   ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
                                                                       

//You have played wonderfully! See you next time!
""")	
	print(goodbye_msg)
	
#MAIN FUNCTION OF THE GAME
#STARTS A GAME LOOP WHICH CONTINUES TO RUN UNTILL THERE'S A WINNER OR A TIE.
#STARTS WITH CALLING GAME HEADER WITH DEFAULT 'begin' ARGUMENT
#GETS INPUT FOR PLAYER 'X'
#CHECKS IF PLAYER 'X' WINS OR IF THERE'S A TIE. 
#IF PLAYER WINS OR THERE'S A TIE CALLS REMATCH FUNC AND BREAKS THE MAIN GAME LOOP
def main(board=board):
	while True:
		game_header()
		get_player_input('X')
		game_header()
		if check_winner_tie('X'):
			rematch()
			break
		get_player_input('O')
		game_header()
		if check_winner_tie('O'):
			rematch()
			break

#calls main() function if the scripts is called from command line/terminal and not imported			
if __name__ == '__main__':
	main()

		
