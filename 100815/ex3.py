# This example aims to count the number of character number in an integer number
import math

# Get the list of character number in an integer number
# @nb: Integer number
# return: list of character number in @nb
def chNumber(nb):
	listChNumber = []
	
	devisor = nb
	while devisor > 0:
		surplus = devisor % 10
		listChNumber.append(surplus)
		devisor = math.floor(devisor / 10)
	return listChNumber
		
if __name__ == "__main__":
	print("Enter an integer number: ")
	m = int(input())
	listNB = chNumber(m)
	print("List: " + str(listNB))
	print("Number of character number in " + str(m)+" is: " + str(len(listNB)))	
