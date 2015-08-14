# Welcome
import random
min = 0
max = 100
nbMax = 10
guessedNb = -1
nbTimes = 0;
print("Wellcome to guess number game. My name is Spy007. What is your name?")
player = input()
print("Hi " + str(player)+". Very nice to meet you.")
number = random.randint(min,max)
print("I am thinking about a number between "+str(min)+" and "+str(max)+".\nTo win the game, you have to guess my number in "+str(nbMax)+" times of guessing")
while nbTimes<nbMax:
	nbTimes=nbTimes+1
	print("Your guess number is: ")
	guessedNb = input()
	guessedNb = int(guessedNb)
	if guessedNb==number:
		break
	elif guessedNb>number:
		print("My number is smaller than "+str(guessedNb))
	else :
		print("My number is bigger than "+str(guessedNb))
if guessedNb==number:
	print("Well done! You have correct number after "+str(nbTimes)+" guessing times.\n Thank you for your time. See you again")
else:
	print("You are failed to guess my number in "+str(nbTimes)+" guessing times. My secret number is: " + str(number)+"\nThank you for your time. See you again!")

