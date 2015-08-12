# This example aims to get sum of all character number in an integer

# Import chNumber function from ex3.py
from ex3 import chNumber

# Get sum of all elements of a list
# @list: list of integer numbers
# return: sum of all elements in @list
def listSum(list):
	sum = 0
	for x in list:
		sum = sum + x
	return sum

print("Enter an integer number: ")
m = int(input())

# Get list character number in m
listNB = chNumber(m)

# Get sum of all elements in listNB
lsum = listSum(listNB)

print("Sum of all character number in " + str(m) + " is: " + str(lsum))

