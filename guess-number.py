# Welcome
import random
print("Wellcome to guess number game. My name is Spy007. What is your name?")
player = input()
print("Hi " + str(player)+". Very nice to meet you.")
number = random.randint(0,100)
print("I am thinking about a number between 0 and 100. Can you guess what is that?")
guessedNb = -1
nbTimes = 0;
while guessedNb!=number:
	nbTimes=nbTimes+1
	print("Your guess number is: ")
	guessedNb = input()
	guessedNb = int(guessedNb)
	if guessedNb>number:
		print("My number is smaller than "+str(guessedNb))
	if guessedNb<number:
		print("My number is bigger than "+str(guessedNb))
	else:
		print("Very good. You have correct number")

print("You have correct number after "+str(nbTimes)+" guessing. Thank you for your time. See you again")

