rules = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}

# Computer move
from random import choice

move = ['rock','paper','scissors']

computer = choice(move)

# Player move
human = input('Enter move (rock, paper, scissors):')

print('Player  :', human)
print('Computer:', computer)

# The winner of a round can be determined by checking the winning conditions
if rules[human] == computer:
    print('You lose!')
elif rules[computer] == human:
    print('You win!')
else:
    print('Draw!')