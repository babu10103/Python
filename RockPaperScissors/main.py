import random
def play():
  user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return 'tie'
  # r > s, s > p, p > r

  if computer == 'r' and user == 's' or computer == 's' and user == 'p' or computer == 'p' and user == 'r':
    return 'Computer Won'
  else:
    return 'User Won'

print(play())