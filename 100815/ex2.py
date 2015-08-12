# This example aims to show the first m prime numbers, with m is a user input.

from ex0 import isPrime

# Input a number:
print("Enter a numer:")
m = int(input())
print("List of " + str(m) + " first prime numbers is:")

# Initialize counter and current number
counter = 0
curNumber = 1

# Repeat until we have m prime numers
while counter < m:

	# Repeat increase current number until we found a prime number
	while not isPrime(curNumber):
		# Increase current number
		curNumber = curNumber + 1

	# Found a prime number
	print("%d "%(curNumber),end="",flush=True)

	# Increase counter - number of prime number
	counter = counter +1

	# Increase current number
	curNumber = curNumber + 1

print("\nEnd!")
