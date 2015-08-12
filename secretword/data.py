import random

# List of secret word
wordlist = ["government","important","different","beneath","early"]

# List of score
scorelist = [-2,-1,0,1,2,5,"skip","lost_all","double","haft"]

# List of player
playerNamelist = []
playerScoreList = []

# Get randomly a secret word
def getSecretWord():
	index = random.randint(len(wordlist))
	return wordlist[index]

# Get randomly a score value - turn the wheel
def getScore():
	index = random.randint(len(scorelist))
	return scorelist[index]

# Show the word with list of open character
def showWord(listCs,word):
	showedword = word
	for x in showedword:
		if showedword.index(x) < 0:
			showedword = showedword.replace(x,"-")
	return showedword

# Initial game
def initGame(playerlist)
	if(len(playerlist)<1):
		print("ERROR: There is must be at least 1 player")
		return
	else:
		for i in range(len(playerlist)):
				
 


# start a game with input list player name
def startGame():
	if(len(playerNameList)<1):
		print("There is must be at least 1 player")
		return
	
