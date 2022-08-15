import random

def guess(x):
  num = random.randint(1, x)
  guess = 0
  while guess != num:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < num:
      print(f'Sorry, guess again. Too low.')
    elif guess > num:
      print(f'Sorry, guess again. Too high.')
  print(f'Yay, congrats. You have guessed the number {num} correctly!!')

def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  val = 0
  while feedback != 'c':
    if low != high:
      val = random.randint(low, high)
    else:
      val = low
    feedback = input(f'Is {val} too high (H), too low (L), or correct (C)??').lower()
    if feedback == 'h':
      high = val - 1
    if feedback == 'l':
      low = val + 1
  print(f'Yay! The computer guessed your numberm, {val}, correctly')

computer_guess(200)
