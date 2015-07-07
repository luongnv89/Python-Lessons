import random
print("\n***** GUESS NUMBER GAME ****")
print("What is your name?")
playerName = input()
print("----> Welcome "+str(playerName)+" to guess number game <-----\n\n")
print("You are thinking about a number. I will guess what it is. \nDo you have a number?\n....\n...\nYes, so let's go!\n")
print("I need to know what is the range of your number")
print("Lowest bound (Minimum):")
min = input()
min = int(min)
print("Highest bound (Maximum):")
max = input()
max = int(max)
print("How many times can I guess?")
nbMax = input()
nbMax = int(nbMax)
print("So your number is between "+str(min)+" and "+str(max)+".\nNow I am going to give you my guessed number.\nPlease let's me know if it bigger or smaller than your number.")
nbTimes = 0
while nbTimes<nbMax:
	nbTimes = nbTimes + 1
	guessedNb = int((min+max)/2)
	print("Is "+str(guessedNb)+" your number? 1-yes or 0-no ")
	userChoose = input()
	userChoose = int(userChoose)
	if userChoose == 1:
		print("So I have your number after "+str(nbTimes)+" times of guessing\n")
		break
	if userChoose == 0:	
		print("Is "+str(guessedNb)+" bigger (1) or smaller(0) than your number?")
		userChoose2 = input()
		userChoose2 = int(userChoose2)
		if userChoose2 == 1:
				max = guessedNb
		if userChoose2 == 0:
				min = guessedNb
if nbTimes<nbMax:
	print("I won! .... ")
else:
	print("Sorry I could not guess your number in "+str(nbMax)+" times of guessing")
print("Thank you for your time. See you again ...")
		

