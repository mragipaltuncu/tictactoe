#Import 'random' module for computer generated random choices
import random

#Define a game board, this one is a 3x3 board, starting from position '0'
board = [0,1,2,
		 3,4,5,
		 6,7,8]

#Resets the board
def reset_board():
	global board 
	board_reset = [0,1,2,
		 3,4,5,
		 6,7,8]

	board = board_reset[:]


#A function to draw game board in a nice format
def draw():
	print('\n')
	print('|',board[0],'|',board[1],'|',board[2],'|')
	print('-------------')
	print('|',board[3],'|',board[4],'|',board[5],'|')
	print('-------------')
	print('|',board[6],'|',board[7],'|',board[8],'|')
	print('\n')	  


#A horrible way to check win conditions, listing all possible win positions. char is Either 'X' or 'O'
def condition_check(char):
	if board[0] == char and board[1] == char and board[2] == char:
		return True

	if board[3] == char and board[4] == char and board[5] == char:
		return True

	if board[6] == char and board[7] == char and board[8] == char:
		return True

	if board[0] == char and board[3] == char and board[6] == char:
		return True

	if board[1] == char and board[4] == char and board[7] == char:
		return True

	if board[2] == char and board[5] ==char and board[8] == char:
		return True

	if board[0] == char and board[4] ==char and board[8] == char:
		return True

	if board[2] == char and board[4] ==char and board[6] == char:
		return True

#A completely useless piece of code to recheck who the winner is 
def win_check(char):
	if condition_check(char) and char == 'X':
		return True
		 
	if condition_check(char) and char == 'O':
		return True

#Main function of the game, starts the game loop.
def main():
	#The main loop of the game which continues to run as long as there's no winner or the board still has playable boxes.
	while True:
		#Draw game board
		draw()

		#Player_choice loop, until player chooses an empty box the loop runs
		while True:
			#Prompt player to pick a box to place 'X'
			player_choice = int(input("Chose a box to place 'X' [0-8] :  "))
			
			#Check if player_choice box is already FULL
			if board[player_choice] != 'X' and board[player_choice] != 'O':
				#Place player choice in the board list and replace the number value with 'X' and break the loop
				board[player_choice] = 'X'
				break
			#If the box is full print a message and loop starts again
			else:
				print("That box is FULL! Choose another!")

		#Check for win condition and reset the board, ask for a rematch
		if win_check('X'):
			print ("You win!")
			draw()
			reset_board()
			cevap = input("Yeniden Oyna ? [E/H]")
			if cevap == 'E' or cevap == 'e':
				main()
			elif cevap == 'H' or cevap == 'h':
				"Teşekkürler.Görüşmek üzere!"
				break


		#Computer_choice loop, until computer randomly chooses an empty box to loop runs
		while True:
			#Random module needs a seed, here the default "system time" is used
			random.seed()
			#Computer uses the seed to randomly pick a number between 0-8
			computer_choice = random.randint(0,8)
			#Check if the computer_choice is already full,if not break the rule
			if board[computer_choice] != 'O' and board[computer_choice] != 'X':
				board[computer_choice] = 'O'
				break	

		#Check for win condition and reset the board, ask for a rematch
		if win_check('O'):
			print ("You lose!")
			draw()
			reset_board()
			cevap = input("New Game ? [Y/N]")
			if cevap == 'Y' or cevap == 'y':
				main()
			elif cevap == 'N' or cevap == 'n':
				"Thank you! See you later!"
				break


if __name__ == '__main__':
	print("\nWelcome to Tic-Tac-Toe")
	main()