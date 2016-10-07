def printhanger(tries,maxtries):
	if tries == maxtries:
		print ("+-----+\n|\n|\n|")
	elif tries == 4:
		print ("+-----+\n|     O\n|\n|")
	elif tries == 3:
		print ("+-----+\n|     O\n|   /[#]\n|")
	elif tries == 2:
		print ("+-----+\n|     O\n|   /[#]\ \n|")
	elif tries == 1:
		print ("+-----+\n|     O\n|   /[#]\ \n|    /")
	else:
		print ("+-----+\n|     O\n|   /[#]\ \n|    / \ ")
	return str(tries)

def address(letter,text):
		w = list(text)
		count = 0
		D = []
		for x in w:
			if letter==x:
				D.append(count)
			count +=1
		return D

import random
l0 = list(open("words.txt"))
l1 = []
for x in l0:
	word = x[:-1]
	l1.append(word)
answer ='p'
while answer.lower()=='p':
	maxtries=5
	tries=maxtries
	print ('\n'*50)
	print ("="*70)
	print ("************************ Welcome to KREMALA ! ************************")
	print ("="*70)
	print ('\n'*3)
	#PHASE 1 !
	a = input('Type g<Enter> or G<Enter> if word will be given by another player: ')
	if a == 'g' or a == 'G':
		word = input('Player don\'t look! 2nd player, type in word, must be in English and\nat least 3 letters long: ')
		print ('\n'*50)
		while word.lower() not in l1:
			word = input("                      ! WRONG INPUT ! \n\n\nThe word must be in English and at least 3 letters long \nPlease try again , type the word: ")
			print ('\n'*50)
	else:
		flag=False
		limits=['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
		while not flag:
			flag=True
			a = input('Type r<Enter> or R<Enter> for word of random length, else give length\nof random word (between 3 and 20):')
			if a =='r' or a =='R':
				word = random.choice(l1)
			elif a in limits:
				length = int(a)
				l2=[]
				for x in l1:
					if len(x)==length:
						l2.append(x)
				word = random.choice(l2)
			else:
				print("\n\n\n\n\n                         ! WRONG INPUT !\n\n\n")
				flag=False

	#PHASE 2!
	choosen = []
	found = []
	print(printhanger(tries,maxtries)+" tries left")
	for i in range(len(word)):
		found.append('_')
	print (' '.join(found))
	print ("="*70)
	wrong_inputs=[' ','!','@','#','$','%','^','&','*','(',')','_','-','=','+','/','?',"'",'"',':','[','{',']','}','~',',','<','.','>','0','1','2','3','4','5','6','7','8','9']
	while tries >0 and found != list(word.upper()):
		print ('Chosen letters: %s' % (choosen))
		guess = input('Guess letter: ')
		while len(guess)!=1 or guess in wrong_inputs:
			print('\n'*7)
			guess =input("                      ! WRONG INPUT ! \n\n\nThe input must be only one English letter!\nNo symbols, No numbers, No Spaces...\nGuess letter: ")
		while guess.upper() in choosen:
			print('\n'*7)
			print ('Chosen letters: %s\n\n\n\n' % (choosen))
			print("            !!! You've chosen this letter already !!!\n\n\n")
			guess = input('Guess letter: ')
		if guess.lower() in word:
			for i in range(len(address(guess.lower(),word))):
				found[address(guess.lower(),word)[i]] = guess.upper()
			if ''.join(found)==word.upper():
				print('\n'*7)
				print('            Congratulations! You\'ve found word \n                      !!! %s !!!\n\n\n' %(word.upper()))
			else:
				print(printhanger(tries,maxtries)+" tries left")
				print (' '.join(found))
				print ("="*70)
				choosen.append(guess.upper())
		else:
			tries -=1
			if tries == 0:
				print(printhanger(tries,maxtries)+" tries left\nSorry! You lost! The word was %s !" %(word.upper()))
			else:
				print(printhanger(tries,maxtries)+" tries left")
				print (' '.join(found))
				print ("="*70)
				choosen.append(guess.upper())
	answer = input("Type P<Enter> or p<Enter> to play again: ")
