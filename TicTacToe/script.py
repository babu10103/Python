start = input('Want to play [y/n]: ')
while start == 'y':
	exec(open('tictactoe.py').read())
	start = input('Want to play again: ')

