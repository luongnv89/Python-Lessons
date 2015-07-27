import random
import time

def t(s):
	for x in range(s):
		time.sleep(1)
		print(".",end="",flush=True)
                

def instro():

	print("Welcome to the dragon world.")
	
	print("It has the good dragon and the bad dragon. And it has 2 cave. One for the good dragon. And other is bad dragon...")
	t(2)
	print("")
	
	print("You are stand in front of 2 cave")
	t(3)
	print("")
	
	print("You must go into  one of the 2 cave")
	t(2)
def choice():
	print(" ")
	
	print("A. First cave   B.Second cave")
	t(2)
	print("")

	print("So, choose a cave. You must to be careful...")

	choose=input()
	
	return choose

def check(c):
	
	print("Are you sureto the "+str(c)+" ? So, let's go!")
	t(2)
	
	print("A dragon step out with a scary sound and...")
	t(4)
	print("")


	x=random.randint(1,2)
	choose=1
	if choose== 'A':
		choose=1
	else:
		choose=2
	if x==choose:
		tru()
	else:
		fal()	
def tru():

		print("Lucky.It's the good dragon. You have treasure.Congratulation. See you again.")
def fal():
	
		print("Oh no, it's the bad dragon. The dragon will eat you. See you at the cemetery.") 

#Pr
def playgame():
	instro()
	a=choice()
	check(a)
#Start
playgame()

 

