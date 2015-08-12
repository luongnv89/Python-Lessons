# This example aims to check an input number is a prime number or not

import math

# Function to check if a number is prime number or not
# @nb: number to check
# return: True if nb is a prime number
#	  False otherwise
def isPrime(nb):
	# If input number is 1 or 2 then it is a prime number
	if nb == 1 or nb == 2:
		return True

	# Searching the devisor of input number. Start from 2 to number - 1
	start = 2
	max = nb - 1
	
	# Repeat until start smaller than max
	while start < max:
		# Check if start is a devisor of nb
		if (nb % start) == 0:
			return False
		else:
			# Update start and max
			start = start +1
			max = math.ceil(nb / start)
	return True

if __name__ == "__main__":
	# Input a number:
	print("Enter a numer:")
	m = int(input())
	if isPrime(m):
		print(str(m)+" is a prime number")
	else:
		print(str(m)+" is not a prime number")
	print("\n End!")
