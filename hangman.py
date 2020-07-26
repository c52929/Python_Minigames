import random
import time
import functionsLists
import xlrd
# import pprint

words=xlrd.open_workbook('hangman_wordsdata/words_data.xlsx').sheet_by_index(1).col_values(0)
# 本当は以下の手順を踏んでいる
# wb=xlrd.open_workbook('hangman_wordsdata/words_data.xlsx')
# ws=wb.sheet_by_index(1)
# col_values=ws.col_values(0)
# words=col_values

alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print('Welcome to Hang Man Game!')

lives=6
lives_gauge=''
guesses=[]
correct_list=[]
correct=words[random.randrange(len(words))].upper()
for i in range(len(correct)):
	correct_list.append(correct[i])

def update_lives_gauge(lives):
	lives_gauge='['
	for i in range(6):
		if i<lives:
			lives_gauge+=' o'
		else:
			lives_gauge+=' x'
	return lives_gauge+' ]'

def update_secret_word():
	info='['
	for i in range(len(correct)):
		if correct[i] in guesses:
			info+=' '+correct[i]
		else:
			info+=' _'
	return info+' ]'

def ask(message):
	new_guess=input(message).upper()
	functionsLists.exit_judge(new_guess)
	if new_guess in guesses:
		ask("You have already guessed '"+new_guess+"'. Guess again: ")
		return()
	elif new_guess in alphabets:
			guesses.append(new_guess)
			time.sleep(0.4)
			if new_guess in correct_list:
				print('Correct!')
			else:
				print("Dang it! '"+new_guess+"' is not used.")
				global lives
				lives-=1
			time.sleep(0.4)
			print('Lives:'+update_lives_gauge(lives)+' Secret Word:'+update_secret_word()+'\n')
	else:
		ask('Answer with an alphabet letter: ')

def turn():
	global lives
	ask('Guess a letter included in the secret word: ')
	info=''
	for i in range(len(update_secret_word())):
		if not(update_secret_word()[i] in ['[',' ',']']):
			info+=update_secret_word()[i]
	time.sleep(0.8)
	if info==correct:
		print('Congratulations! You hit the word!\n')
	elif lives<1:
		if functionsLists.ask_try_again('You lost lives...', False):
			lives=6
			print('Lives:'+update_lives_gauge(lives)+' Secret Word:'+update_secret_word())
			turn()
		else:
			print("The answer was '"+correct+"'. See you...\n")
	else:
		turn()
		return()

print('Lives:'+update_lives_gauge(lives)+' Secret Word:'+update_secret_word())
turn()