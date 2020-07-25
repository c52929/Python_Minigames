import random
import time

import functionsLists

hands_kind=['ROCK','PAPER','SCISSORS','R','P','S','1','2','3']
result=['','']

def ask(message):
	result[0]=input(message).upper()
	functionsLists.exit_judge(result[0])
	if result[0] in hands_kind:
		result[0]=hands_kind[hands_kind.index(result[0])%3]
	else:
		ask('Choose and type one of Rock(R, 1), Paper(P, 2) or Scissors(S, 3) : ')
		return()
	result[1]=hands_kind[random.randrange(3)]

def turn(message):
	ask(message)
	time.sleep(0.5)
	print('YOU: '+result[0]+' - '+result[1]+' :com')
	time.sleep(1)
	if hands_kind.index(result[0])==hands_kind.index(result[1]):
		turn('Draw! Rock(R, 1), Paper(P, 2) or Scissors(S, 3)? : ')
	elif hands_kind.index(result[0])-1==hands_kind.index(result[1]) or hands_kind.index(result[0])+2==hands_kind.index(result[1]):
		if functionsLists.ask_try_again('You win!'):
			turn('Which do you show, Rock(R, 1), Paper(P, 2) or Scissors(S, 3)? : ')
	else:
		if functionsLists.ask_try_again('You lose.'):
			turn('Which do you show, Rock(R, 1), Paper(P, 2) or Scissors(S, 3)? : ')
	return()

print('Welcome to Janken!')
turn('Which do you show, Rock(R, 1), Paper(P, 2) or Scissors(S, 3)? : ')
print()