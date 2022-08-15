import random
from words import words
import string

def get_valid_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words) 

	return word

def hangman():
	word = get_valid_word(words).upper()
	word_chars = set(word)
	alphabet = set(string.ascii_uppercase)
	used_letters = set()

	lives = 6
	while len(word_chars) > 0 and lives != 0:

		print('You have ', lives, ' lives left and you have used following letters: ', ' '.join(used_letters))

		word_status = [letter if letter in used_letters else '-' for letter in word]

		print('Current word: ', ' '.join(word_status))

		letter = input('Guess a letter: ').upper()

		if letter in alphabet - used_letters:
			used_letters.add(letter)
			print(used_letters)
			if letter in word_chars:
				word_chars.remove(letter)
			else:
				lives = lives - 1
				print('letter is not in word.')

		elif letter in used_letters:
			print('You already used that letter. Please guess different one!!')
		else:
			print('Invalid Character. Please Try again!!')

	if lives == 0:
		print('You died, sorry. The word was: ', word)
	else:
		print('You guessed the word ', word, '!!')

hangman()