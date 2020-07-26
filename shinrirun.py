import random
import time

import functionsLists

how_gone=[0,0,0,0]
want_go=[0,0,0,0]
go_steps=[0,0,0,0]
players=['YOU:','com1','com2','com3']

def ask():
	check=input('How many steps do you walk, 1, 3 or 5? : ')
	functionsLists.exit_judge(check)
	if check in ['1','3','5']:
		want_go[0]=int(check)
	else:
		ask()
		return
	for i in range(3):
		want_go[i+1]=random.randrange(1,6,2)

def one_turn():
	ask()

	for i in range(4):
		check=want_go[i]
		want_go[i]=''
		if check in want_go:
			go_steps[i]='±0'
		else:
			go_steps[i]='+'+str(check)
			how_gone[i]+=check
		want_go[i]=check

	print('Result: '+str(want_go)+' => ['+go_steps[0]+', '+go_steps[1]+', '+go_steps[2]+', '+go_steps[3]+']')

	time.sleep(1)

	for i in range(4):
		stand_by=players[i]+':['
		for j in range(20):
			if j<how_gone[i]:
				stand_by+='#'
			else:
				stand_by+='-'
		stand_by+=']'
		print(stand_by)

	print()
	
	for i in range(4):
		if how_gone[i]>=20:
			return
	
	time.sleep(0.5)
	one_turn()

print('Welcome to Shinri Run!')

one_turn()

if how_gone[0]>how_gone[1] and how_gone[0]>how_gone[2] and how_gone[0]>how_gone[3]:
	if functionsLists.ask_try_again('Congratulations! You win!', True):
		how_gone=[0,0,0,0]
		one_turn()
else:
	if functionsLists.ask_try_again('Finished! You lose.', True):
		how_gone=[0,0,0,0]
		one_turn()