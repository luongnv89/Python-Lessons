import random
print("\n\n")
print("***** GUESS NUMBER GAME ****")
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
print("So your number is between "+str(min)+" and "+str(max)+".\n Now I am going to give you my guessed number.\n Please let's me know if it bigger or smaller than your number.")
correct = False
nbTimes = 0
while correct==False:
	nbTimes = nbTimes + 1
	guessedNb = random.randint(min,max)
	print("Is "+str(guessedNb)+" your number? 1-yes or 0-no ")
	userChoose = input()
	userChoose = int(userChoose)
	if userChoose == 1:
		print("So I have your number after "+str(nbTimes)+" times of guessing\n")
		correct = True
	if userChoose == 0:	
		print("Is "+str(guessedNb)+" bigger (1) or smaller(0) than your number?")
		userChoose2 = input()
		userChoose2 = int(userChoose2)
		if userChoose2 == 1:
				max = guessedNb-1
		if userChoose2 == 0:
				min = guessedNb+1
print("Thank you for your time. See you again ...")
		

