import dragonrealm

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
        dragonrealm.playGame()
        print("\nYou want to play again: 'yes' or 'no': ",end="")
        playAgain = input()
dragonrealm.goodbye()
