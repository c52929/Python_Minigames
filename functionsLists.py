answer_yes=['y','ye','yes','yea','yeah','yu','yup','yp','ya','yay','yo']
answer_no=['n','no','not','nop','nope','np','npe']

answer_exit=['exit','quit','end']

def exit_judge(answer):
	if answer.lower() in answer_exit:
		print('See you...\n')
		exit()

def ask_try_again(message):
	try_again=input(message+' Try again? Y/N: ')
	exit_judge(try_again)
	if try_again.lower() in answer_yes:
		print()
		return(True)
	elif try_again.lower() in answer_no:
		print('See you...\n')
		exit()
	else:
		ask_try_again('Answer Y or N.')
		return()