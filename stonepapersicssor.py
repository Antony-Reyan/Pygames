from random import choice
import time
print('...stone...\n...paper...\n...scissors...')
print("")
print("TYPE 'OUIT' OR 'Q' TO END THE GAME ")
print("")
print("TYPE 'SCORE' TO CHECK LIVE SCORE")
player_wins=0
computer_wins=0
elements={

	'stone': '''  
	    _______
	---'   ____)  
	      (_____)  
	      (_____)  
	      (____)
	---.__(___)  
	''',


	'paper': '''  
	    _______
	---'   ____)____  
	          ______)  
	          _______)  
	         _______)
	---.__________)  
	''',
	'scissors' : '''  
	    _______
	---'   ____)____  
	          ______)  
	       __________)  
	      (____)
	---.__(___)  
	'''
}

while True:

	element=['stone','paper','scissors']
	computer=choice(element)
	print("")
	print("")
	time.sleep(1)
	player=input("ENTER YOUR CHOICE		:").lower()
	print("")


	if player=='quit' or player=='q':
		time.sleep(0.5)
		print(f'FINAL SCORE:\nYOUR SCORE:{player_wins}\nCOMPUTER SCORE:{computer_wins}\n.................')
		if player_wins>computer_wins:
			print("😉 CONGRATE YOU WIN THIS MATCH")
		elif player_wins==computer_wins:
			print("😐 TIE")
		else:
			print("😞 YOU LOSE") 
		print("GOOD BYE!")

		break


	elif player=='stone'or player=='paper'or player=='scissors':
		time.sleep(0.3)

		if player =='stone' and computer=='stone':
			print(f'Your choice:{elements[player]} \ncomputer choice:{elements[computer]}\nIT\'S TIE')
		elif player =='paper' and computer=='paper':
			print(f'Your choice:{elements[player]} \ncomputer choice:{elements[computer]}\nIT\'S TIE')
		elif player =='scissors' and computer=='scissors':
			print(f'Your choice:{elements[player]} \ncomputer choice:{elements[computer]}\nIT\'S TIE')


		elif player =='stone' and computer=='scissors':
			print(f'Your choice:{elements[player]} \ncomputer choice:{elements[computer]}\nYOU WIN')
			player_wins+=1
		elif player =='paper' and computer=='stone':
			print(f'Your choice:{elements[player]} \ncomputer choice:{elements[computer]}\nYOU WIN')
			player_wins+=1
		elif player =='scissors' and computer=='paper':
			print(f'Your choice:{elements[player]} \ncomputer choice:{elements[computer]}\nYOU WIN')
			player_wins+=1

		else:
			print(f'Your choice:{elements[player]} \ncomputer choice:{elements[computer]}\nYOU LOSE')
			computer_wins+=1



	elif player=='score':
		time.sleep(0.3)
		print(f'YOUR LIVE SCORE IS:\nYOUR SCORE:{player_wins}\nCOMPUTER SCORE:{computer_wins} ')


	else:
		print("❗PLEASE ENTER THE VALIDE CHOICE")




